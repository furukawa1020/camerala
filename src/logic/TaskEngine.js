export class TaskEngine {
    constructor(canvasElement) {
        this.canvas = canvasElement;
        this.ctx = canvasElement.getContext('2d');
        this.onTrialData = null; // Callback for logging

        // Task State
        this.difficulty = 0.5; // 0.0 to 1.0 (1.0 = easiest)
        this.config = {
            fixationDur: 500,
            stimulusDur: 200, // limited time
            feedbackDur: 500,
            baseDifficulty: 20 // degrees tilt
        };

        this.currentTrial = null;
        this.state = 'IDLE'; // IDLE, FIXATION, STIMULUS, RESPONSE, FEEDBACK
        this.resize();
        window.addEventListener('resize', this.resize.bind(this));
    }

    resize() {
        this.canvas.width = 800; // Fixed cognitive space
        this.canvas.height = 600;
    }

    startBlock(condition) {
        this.blockCondition = condition;
        // Reset difficulty if needed or keep carry-over
        // Usually keep carry-over to maintain stability
    }

    async runTrial(trialId, trialConfig) {
        this.currentTrial = {
            id: trialId,
            startTime: performance.now(),
            stimulus: Math.random() > 0.5 ? 'RIGHT' : 'LEFT', // Tilted Right or Left
            difficulty: this.difficulty,
            ...trialConfig // block info etc
        };

        // 1. Fixation
        this.state = 'FIXATION';
        this.draw();
        await this.wait(this.config.fixationDur);

        // 2. Stimulus
        this.state = 'STIMULUS';
        this.draw();
        const stimStart = performance.now();

        // 3. Wait for Response (or timeout)
        const response = await this.waitForResponse();
        const rt = performance.now() - stimStart;

        // 4. Feedback
        const isCorrect = response === this.currentTrial.stimulus;
        this.state = 'FEEDBACK';
        this.draw(isCorrect);

        // Adapt Difficulty (1-up 2-down or simple tracking)
        // Simple: Correct -> Harder, Incorrect -> Easier
        if (isCorrect) {
            this.difficulty = Math.max(0.01, this.difficulty * 0.95); // getting harder (smaller tilt)
        } else {
            this.difficulty = Math.min(1.0, this.difficulty * 1.2); // getting easier
        }

        // Log logic (user prompt specifically asked for closed loop)
        // We log the *result*
        const result = {
            ...this.currentTrial,
            response,
            rt,
            correct: isCorrect,
            difficulty_next: this.difficulty
        };
        if (this.onTrialData) this.onTrialData(result);

        await this.wait(this.config.feedbackDur);
        this.state = 'IDLE';
        this.draw();
    }

    waitForResponse() {
        return new Promise(resolve => {
            const handler = (e) => {
                if (e.key.toLowerCase() === 'f') { // Left
                    cleanup();
                    resolve('LEFT');
                } else if (e.key.toLowerCase() === 'j') { // Right
                    cleanup();
                    resolve('RIGHT');
                }
            };

            const cleanup = () => window.removeEventListener('keydown', handler);
            window.addEventListener('keydown', handler);

            // Can add timeout here if needed
        });
    }

    wait(ms) {
        return new Promise(r => setTimeout(r, ms));
    }

    draw(feedbackState) {
        // Clear
        this.ctx.fillStyle = '#1a1a1a';
        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);

        const cx = this.canvas.width / 2;
        const cy = this.canvas.height / 2;

        if (this.state === 'FIXATION') {
            this.ctx.fillStyle = 'white';
            this.ctx.fillRect(cx - 5, cy - 5, 10, 10);
        }
        else if (this.state === 'STIMULUS') {
            // Draw Gabor-like patch (or just a Gabor/Line)
            this.ctx.save();
            this.ctx.translate(cx, cy);
            // Tilt: Positive = Right, Negative = Left
            const tilt = this.currentTrial.stimulus === 'RIGHT' ? 1 : -1;
            const angle = tilt * (this.difficulty * this.config.baseDifficulty) * (Math.PI / 180);

            this.ctx.rotate(angle);

            // Draw Grating
            this.ctx.strokeStyle = 'white';
            this.ctx.lineWidth = 4;
            for (let i = -50; i <= 50; i += 10) {
                this.ctx.beginPath();
                this.ctx.moveTo(i, -50);
                this.ctx.lineTo(i, 50);
                this.ctx.stroke();
            }

            // Mask circle
            this.ctx.globalCompositeOperation = 'destination-in';
            this.ctx.beginPath();
            this.ctx.arc(0, 0, 50, 0, Math.PI * 2);
            this.ctx.fill();

            this.ctx.restore();
        }
        else if (this.state === 'FEEDBACK') {
            const color = feedbackState ? '#00cc66' : '#ff3333';
            this.ctx.fillStyle = color;
            this.ctx.beginPath();
            this.ctx.arc(cx, cy, 10, 0, Math.PI * 2);
            this.ctx.fill();
        }
    }
}
