import { FaceMesh } from '@mediapipe/face_mesh';

export class CameraManager {
  constructor(videoElement, canvasElement) {
    this.video = videoElement;
    this.canvas = canvasElement;
    this.ctx = canvasElement.getContext('2d');
    this.faceMesh = null;
    this.isReady = false;
    this.onResults = null; // Callback for when results are ready
  }

  async initialize() {
    // 1. Setup Camera
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { 
          width: { ideal: 640 }, 
          height: { ideal: 480 },
          frameRate: { ideal: 30 }
        },
        audio: false
      });
      this.video.srcObject = stream;
      await new Promise((resolve) => {
        this.video.onloadedmetadata = () => {
          this.video.play(); // Warning: promise handling for play()
          resolve();
        };
      });
      
      this.canvas.width = this.video.videoWidth;
      this.canvas.height = this.video.videoHeight;

    } catch (e) {
      console.error("Camera failed:", e);
      throw new Error("Could not access camera");
    }

    // 2. Setup FaceMesh
    this.faceMesh = new FaceMesh({locateFile: (file) => {
      return `https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh/${file}`;
    }});

    this.faceMesh.setOptions({
      maxNumFaces: 1,
      refineLandmarks: true, // For iris/eyes
      minDetectionConfidence: 0.5,
      minTrackingConfidence: 0.5
    });

    this.faceMesh.onResults(this.handleResults.bind(this));

    // Start processing loop
    this.processFrame();
    this.isReady = true;
  }

  handleResults(results) {
    // Draw landmarks for debug
    this.ctx.save();
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    // (Optional: Draw video frame if needed, but video element is under it)
    // this.ctx.drawImage(results.image, 0, 0, this.canvas.width, this.canvas.height);
    
    if (results.multiFaceLandmarks && results.multiFaceLandmarks.length > 0) {
       // Just draw a simple bounding box or mesh for confidence
       // For now, we delegate the raw results to the callback
       if (this.onResults) this.onResults(results);
       
       // Debug visual: Green box around face
       // Note: implementation of drawing logic would go here
    }
    this.ctx.restore();
  }

  async processFrame() {
    if (!this.video.paused && !this.video.ended) {
      await this.faceMesh.send({image: this.video});
    }
    requestAnimationFrame(this.processFrame.bind(this));
  }
}
