import JSZip from 'jszip';

export class DataLogger {
    constructor() {
        this.sessionData = {
            metadata: {},
            blocks: [],
            trials: [],
            windows: [], // Features aggregated by window
            subjective: []
        };

        this.windowBuffer = []; // Buffer for raw frames to be aggregated
        this.aggregatedWindows = []; // Completed windows
        this.windowConfig = { size: 10000, overlap: 5000 };
        this.nextWindowStartTime = -1;
        this.startTime = Date.now();
    }

    startSession(blockPlan) {
        this.sessionData.metadata = {
            sessionId: (typeof crypto !== 'undefined' && crypto.randomUUID) ? crypto.randomUUID() : `session_${Date.now()}`,
            startTime: new Date().toISOString(),
            userAgent: navigator.userAgent,
            blockPlan: blockPlan
        };
    }

    // Called every frame by main loop
    logFrameFeatures(features, condition, blockId) {
        const now = performance.now();

        // 1. Raw Logging (still useful)
        this.windowBuffer.push({
            t: now,
            c: condition || 'NONE',
            b: blockId,
            ...features
        });

        // 2. Windowing Logic
        // Initialize start time if needed
        if (this.nextWindowStartTime < 0) this.nextWindowStartTime = now;

        // Check if we have enough data for a window (current time > start + size)
        // We process "past" windows. 
        // Ideally this is done in post-processing, but requirement FR-12 implies saving "windows".
        // We will scan the buffer for the target window range.

        // Simple sliding window: Check if we have covered the current target window
        const windowEnd = this.nextWindowStartTime + this.windowConfig.size;

        if (now >= windowEnd) {
            // Extract window data
            const windowFrames = this.windowBuffer.filter(f => f.t >= this.nextWindowStartTime && f.t < windowEnd);

            if (windowFrames.length > 0) {
                // Find trials overlapping this window
                // We need access to trials. 
                // Since DataLogger holds `this.sessionData.trials`, we can filter them.
                const trialsInWindow = this.sessionData.trials.filter(t => t.timestamp >= this.nextWindowStartTime && t.timestamp < windowEnd);

                this.aggregateWindow(windowFrames, trialsInWindow, this.nextWindowStartTime, windowEnd, blockId, condition);
            }

            // Advance
            this.nextWindowStartTime += (this.windowConfig.size - this.windowConfig.overlap);
        }
    }

    aggregateWindow(frames, trials, start, end, blockId, condition) {
        // Calculate means/variances for Signals
        const count = frames.length;
        const features = {};
        const keys = ['roival', 'motion', 'ear', 'quality', 'exposure_fluc'];

        keys.forEach(k => {
            const sum = frames.reduce((acc, cur) => acc + (cur[k] || 0), 0);
            features['mean_' + k] = sum / count;
        });

        // Calculate Behavior Metrics (FR-12: Aggregated behavior)
        let meanRT = null;
        let accuracy = null;
        let errorCount = 0;

        if (trials && trials.length > 0) {
            const rts = trials.map(t => t.rt);
            meanRT = rts.reduce((a, b) => a + b, 0) / rts.length;

            const correctCount = trials.filter(t => t.correct).length;
            accuracy = correctCount / trials.length;
            errorCount = trials.length - correctCount;
        }

        this.aggregatedWindows.push({
            window_id: (typeof crypto !== 'undefined' && crypto.randomUUID) ? crypto.randomUUID() : `win_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`,
            block_id: blockId,
            condition: condition,
            start_time: start,
            end_time: end,
            frame_count: count,
            ...features,
            // Behavior
            mean_rt: meanRT,
            accuracy: accuracy,
            error_count: errorCount,
            trial_count: trials.length
        });
    }

    logTrial(data) {
        this.sessionData.trials.push(data);
    }

    logBlockStart(id, condition) {
        this.sessionData.blocks.push({ type: 'START', id, condition, time: performance.now() });
    }

    logBlockEnd(id) {
        this.sessionData.blocks.push({ type: 'END', id, time: performance.now() });
    }

    logSubjective(blockId, condition, ratings) {
        this.sessionData.subjective.push({
            blockId, condition, ...ratings, time: performance.now()
        });
    }

    save() {
        const zip = new JSZip();

        // Metadata
        zip.file("metadata.json", JSON.stringify(this.sessionData.metadata, null, 2));

        // Trials
        zip.file("trials.csv", this.toCSV(this.sessionData.trials));

        // Subjective
        zip.file("subjective.csv", this.toCSV(this.sessionData.subjective));

        // Blocks
        zip.file("blocks.csv", this.toCSV(this.sessionData.blocks));

        // Windows
        zip.file("windows.csv", this.toCSV(this.aggregatedWindows));

        // Features (Raw)
        zip.file("features_raw.csv", this.toCSV(this.windowBuffer));

        zip.generateAsync({ type: "blob" })
            .then(function (content) {
                // Trigger download
                const a = document.createElement("a");
                a.href = URL.createObjectURL(content);
                a.download = `cammind_session_${Date.now()}.zip`;
                a.click();
            });
    }

    toCSV(array) {
        if (!array || array.length === 0) return "";
        const headers = Object.keys(array[0]);
        const rows = array.map(obj => headers.map(h => JSON.stringify(obj[h])).join(","));
        return [headers.join(","), ...rows].join("\n");
    }
}
