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

        // 3. ROI Brightness (For rPPG potential)
        // We need to sample the video frame pixels.
        // This requires drawing the video to a canvas or using the existing canvas context if accessible.
        // For prototype, we might skip raw pixel access if performance is tight, 
        // but USER requested "Bright/Hue change".
        // We will assume the CameraManager writes to a canvas we can read, OR we create a small offscreen canvas here.
        const roiBrightness = this.sampleROIBrightness(videoElement, landmarks);

        this.features = {
            roival: roiBrightness,
            motion: motion,
            blink: isBlinking,
            ear: ear,
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

    sampleROIBrightness(video, landmarks) {
        // Simplified: Just sample the center of the forehead
        // Forehead approx index: 151
        // We create a tiny canvas to extract pixel data only if requested, 
        // to avoid layout thrashing, we'll keep a persistent canvas.
        if (!this.canvas) {
            this.canvas = document.createElement('canvas');
            this.canvas.width = 30; // 30x30 ROI
            this.canvas.height = 30;
            this.ctx = this.canvas.getContext('2d', { willReadFrequently: true }); // optimize
        }

        const p = landmarks[151]; // Forehead
        // Coordinates are normalized 0-1
        const x = Math.floor(p.x * video.videoWidth);
        const y = Math.floor(p.y * video.videoHeight);

        try {
            // Draw just the ROI
            this.ctx.drawImage(video, x - 15, y - 15, 30, 30, 0, 0, 30, 30);
            const frame = this.ctx.getImageData(0, 0, 30, 30);
            const data = frame.data;
            let sum = 0;
            // Green channel only (usually best for PPG)
            for (let i = 1; i < data.length; i += 4) {
                sum += data[i];
            }
            return sum / (data.length / 4);
        } catch (e) {
            return 0;
        }
    }
}
