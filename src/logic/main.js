import './css/main.css';
import { CameraManager } from './logic/CameraManager.js';
import { FeatureExtractor } from './logic/FeatureExtractor.js';
import { TaskEngine } from './logic/TaskEngine.js';
import { SessionManager } from './logic/SessionManager.js';
import { DataLogger } from './logic/DataLogger.js';
import { DOMManager } from './ui/DOMManager.js';
// import Stats from 'stats.js'; // Optional

async function main() {
  // Init Components
  const videoEl = document.getElementById('input-video');
  const previewCanvas = document.getElementById('output-canvas');
  const taskCanvas = document.getElementById('task-canvas');

  const ui = new DOMManager();
  const camera = new CameraManager(videoEl, previewCanvas);
  const extractor = new FeatureExtractor();
  const task = new TaskEngine(taskCanvas);
  const logger = new DataLogger();
  const session = new SessionManager(task, ui, logger);

  // Hook up Task logging
  task.onTrialData = (data) => {
    logger.logTrial(data);
  };

  // Main Loop State
  let lastTime = performance.now();
  let frameCount = 0;
  let fps = 0;

  // Camera Callback (runs on every FaceMesh result, ~30fps)
  camera.onResults = (results) => {
    const now = performance.now();
    frameCount++;
    if (now - lastTime >= 1000) {
      fps = frameCount;
      frameCount = 0;
      lastTime = now;
    }

    // Extract Features
    const features = extractor.extract(results, videoEl);

    // Log Features (Continuous)
    // Only if session is running? Or always?
    // User req: "All timestamps synchronized". logging continuous is best.
    if (session.isPlaying) {
      const currentBlock = session.currentBlockIndex;
      const currentCond = session.blocks[currentBlock] || 'PRE_SESSION';
      logger.logFrameFeatures(features, currentCond, currentBlock);
    }

    // Update UI
    ui.updateStatus(fps, features.quality > 0, session.isPlaying ? "RUNNING" : "IDLE");

    if (!session.isPlaying) {
      // Calibration Mode
      ui.updateCalibration(features.roival, features.quality > 0);
    }
  };

  // Start Button Logic
  const startSession = () => {
    document.getElementById('calibration-overlay').classList.add('hidden');
    session.start();
  };

  document.getElementById('btn-start-session').addEventListener('click', startSession);

  // Force Start
  document.getElementById('btn-force-start').addEventListener('click', () => {
    console.warn("Force starting session without quality checks.");
    startSession();
  });

  // Init Camera
  await camera.initialize();
}

main();
