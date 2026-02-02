export class SessionManager {
    constructor(taskEngine, uiManager, dataLogger) {
        this.task = taskEngine;
        this.ui = uiManager;
        this.logger = dataLogger;

        this.conditions = ['THREAT', 'CHALLENGE', 'NEUTRAL'];
        this.blocks = [];
        this.currentBlockIndex = -1;
        this.isPlaying = false;

        this.config = {
            numBlocks: 6, // Reduced for prototype (2 of each)
            trialsPerBlock: 10
        };
    }

    initSession() {
        // Randomize blocks with no more than 2 consecutive same conditions
        this.blocks = this.generateBlockSequence(this.config.numBlocks, this.conditions);
        this.currentBlockIndex = 0;
        this.logger.startSession(this.blocks);
    }

    generateBlockSequence(n, conditions) {
        let seq = [];
        for (let i = 0; i < n; i++) {
            seq.push(conditions[i % conditions.length]);
        }
        // Simple shuffle
        seq.sort(() => Math.random() - 0.5);
        return seq;
    }

    async start() {
        this.initSession();
        this.isPlaying = true;
        await this.runSequence();
    }

    async runSequence() {
        while (this.currentBlockIndex < this.blocks.length && this.isPlaying) {
            const condition = this.blocks[this.currentBlockIndex];

            // 1. Show Instruction
            await this.ui.showInstruction(condition);

            // 2. Run Block
            this.logger.logBlockStart(this.currentBlockIndex, condition);
            this.task.startBlock(condition);

            for (let i = 0; i < this.config.trialsPerBlock; i++) {
                if (!this.isPlaying) break;
                await this.task.runTrial(i, {
                    blockId: this.currentBlockIndex,
                    condition: condition
                });
            }
            this.logger.logBlockEnd(this.currentBlockIndex);

            // 3. Subjective Rating
            const ratings = await this.ui.showSubjectiveRating();
            this.logger.logSubjective(this.currentBlockIndex, condition, ratings);

            this.currentBlockIndex++;
        }

        if (this.isPlaying) {
            this.finish();
        }
    }

    finish() {
        this.isPlaying = false;
        this.logger.save();
        alert("Session Complete! Data downloaded.");
    }
}
