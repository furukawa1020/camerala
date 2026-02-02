export class DOMManager {
    constructor() {
        this.overlays = {
            calibration: document.getElementById('calibration-overlay'),
            instruction: document.getElementById('block-instruction'),
            subjective: document.getElementById('subjective-overlay')
        };

        this.elements = {
            fps: document.getElementById('fps-display'),
            face: document.getElementById('face-status'),
            mode: document.getElementById('mode-display'),
            calibBright: document.getElementById('calib-bright'),
            calibFace: document.getElementById('calib-face'),
            btnStart: document.getElementById('btn-start-session'),
            btnBlock: document.getElementById('btn-start-block'),
            btnSubjective: document.getElementById('btn-submit-subjective'),
            instrTitle: document.getElementById('instruction-title'),
            instrText: document.getElementById('instruction-text')
        };

        // Text Content
        this.texts = {
            'THREAT': "This task is to evaluate your capabilities. Please perform as fast and accurately as possible.",
            'CHALLENGE': "This task is for practice. Feel free to explore your own pace. Mistakes are fine.",
            'NEUTRAL': "Please follow the instructions on the screen."
        };
    }

    updateStatus(fps, faceDetected, phase) {
        this.elements.fps.textContent = fps.toFixed(1);
        this.elements.face.textContent = faceDetected ? "OK" : "LOST";
        this.elements.face.style.color = faceDetected ? "#00f0ff" : "red";
        this.elements.mode.textContent = phase;
    }

    updateCalibration(brightness, faceDetected) {
        this.elements.calibBright.textContent = brightness.toFixed(1);
        this.elements.calibFace.textContent = faceDetected ? "OK" : "No Face";

        if (faceDetected) {
            this.elements.btnStart.disabled = false;
        } else {
            this.elements.btnStart.disabled = true;
        }
    }

    hideAllOverlays() {
        Object.values(this.overlays).forEach(el => el.classList.add('hidden'));
    }

    showInstruction(condition) {
        return new Promise(resolve => {
            this.hideAllOverlays();
            this.overlays.instruction.classList.remove('hidden');
            this.elements.instrTitle.textContent = condition;
            this.elements.instrText.textContent = this.texts[condition];

            const handler = () => {
                this.elements.btnBlock.removeEventListener('click', handler);
                this.overlays.instruction.classList.add('hidden');
                resolve();
            };
            this.elements.btnBlock.addEventListener('click', handler);
        });
    }

    showSubjectiveRating() {
        return new Promise(resolve => {
            this.hideAllOverlays();
            this.overlays.subjective.classList.remove('hidden');

            // Reset sliders
            document.getElementById('slider-appraisal').value = 0;
            document.getElementById('slider-valence').value = 0;
            document.getElementById('slider-utility').value = 0;

            const handler = () => {
                this.elements.btnSubjective.removeEventListener('click', handler);
                const data = {
                    appraisal: document.getElementById('slider-appraisal').value,
                    valence: document.getElementById('slider-valence').value,
                    utility: document.getElementById('slider-utility').value
                };
                this.overlays.subjective.classList.add('hidden');
                resolve(data);
            };
            this.elements.btnSubjective.addEventListener('click', handler);
        });
    }
}
