export class FeatureExtractor {
    constructor() {
        this.prevLandmarks = null;
        this.features = {
            roival: 0, // ROI brightness (proxy for rPPG)
            motion: 0, // Optical flow / Movement
            blink: 0,  // Eye Aspect Ratio or blink detected
            quality: 0 // Confidence
        };
    }

    extract(results, videoElement) {
        if (!results.multiFaceLandmarks || results.multiFaceLandmarks.length === 0) {
            return { ...this.features, quality: 0 };
        }

        const landmarks = results.multiFaceLandmarks[0];

        // 1. Motion (Simple L2 diff from previous frame's landmarks)
        let motion = 0;
        if (this.prevLandmarks) {
            // Check a few key points (nose, chin) for global head movement
            const nose = landmarks[1]; // Nose tip
            const prevNose = this.prevLandmarks[1];
            motion = Math.sqrt(
                Math.pow(nose.x - prevNose.x, 2) +
                Math.pow(nose.y - prevNose.y, 2)
            );
        }
        this.prevLandmarks = landmarks;

        // 2. Blink (EAR - Eye Aspect Ratio)
        // Map points: Left Eye [33, 160, 158, 133, 153, 144] (approx)
        const leftEye = [33, 160, 158, 133, 153, 144];
        const ear = this.calculateEAR(landmarks, leftEye);
        const isBlinking = ear < 0.25 ? 1 : 0; // Threshold

        // 3. ROI Brightness & Exposure Fluctuation (FR-11a)
        // We need whole frame brightness for exposure check
        const { roiLimit, frameAvg } = this.sampleBrightness(videoElement, landmarks);

        // Simple exposure fluctuation: delta from previous frame (or rolling variance)
        let exposureFluc = 0;
        if (this.prevFrameAvg !== undefined) {
            exposureFluc = Math.abs(frameAvg - this.prevFrameAvg);
        }
        this.prevFrameAvg = frameAvg;

        this.features = {
            roival: roiLimit,
            motion: motion,
            blink: isBlinking,
            ear: ear,
            exposure_fluc: exposureFluc, // New Metric
            quality: 1 // Face detected
        };

        return this.features;
    }

    calculateEAR(landmarks, indices) {
        // EAR = (|p2-p6| + |p3-p5|) / (2 * |p1-p4|)
        // Verticals: 160-144, 158-153. Horizontal: 33-133
        const p2 = landmarks[indices[1]];
        const p6 = landmarks[indices[5]];
        const p3 = landmarks[indices[2]];
        const p5 = landmarks[indices[4]];
        const p1 = landmarks[indices[0]];
        const p4 = landmarks[indices[3]];

        const dist = (pA, pB) => Math.hypot(pA.x - pB.x, pA.y - pB.y);

        return (dist(p2, p6) + dist(p3, p5)) / (2 * dist(p1, p4));
    }

    sampleBrightness(video, landmarks) {
        if (!this.canvas) {
            this.canvas = document.createElement('canvas');
            // We need a decent size to estimate whole frame brightness, 
            // but performance matters. 64x48 is enough for "Global Brightness".
            this.canvas.width = 64;
            this.canvas.height = 48;
            this.ctx = this.canvas.getContext('2d', { willReadFrequently: true });
        }

        try {
            // Draw downscaled frame
            this.ctx.drawImage(video, 0, 0, this.canvas.width, this.canvas.height);
            const data = this.ctx.getImageData(0, 0, this.canvas.width, this.canvas.height).data;

            // 1. Whole Frame Avg (Green channel is fine proxy for luminance)
            let sum = 0;
            for (let i = 1; i < data.length; i += 4) {
                sum += data[i];
            }
            const frameAvg = sum / (data.length / 4);

            // 2. ROI (Forehead)
            // Map normalized landmark to canvas coords
            const p = landmarks[151];
            const x = Math.floor(p.x * this.canvas.width);
            const y = Math.floor(p.y * this.canvas.height);

            // Sample 3x3 at minimal
            let roiSum = 0;
            let roiCount = 0;
            for (let dy = -1; dy <= 1; dy++) {
                for (let dx = -1; dx <= 1; dx++) {
                    const currentX = x + dx;
                    const currentY = y + dy;
                    if (currentX >= 0 && currentX < this.canvas.width &&
                        currentY >= 0 && currentY < this.canvas.height) {
                        const idx = (currentY * this.canvas.width + currentX) * 4;
                        roiSum += data[idx + 1]; // Green channel
                        roiCount++;
                    }
                }
            }
            const roiLimit = roiCount > 0 ? roiSum / roiCount : 0;

            return { roiLimit, frameAvg };
        } catch (e) {
            console.error("Error sampling brightness:", e);
            return { roiLimit: 0, frameAvg: 0 };
        }
    }
}
