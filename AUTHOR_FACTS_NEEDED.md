# Author-Confirmed Facts Used in Revision

All previously listed author facts for hardware, environment, and the
face-tracking threshold have been resolved in `paper_his_revision.tex`.

## Hardware / Software

- PC model: mouse Computer G-Tune P517G60ZO21CNHWT.
- CPU: Intel Core i7-13620H.
- GPU: NVIDIA GeForce RTX 5060 Laptop GPU.
- RAM: 32 GB.
- Storage: 1 TB SSD.
- OS: Windows 11 Home 64-bit.
- Webcam: built-in laptop webcam.
- Browsers: Mozilla Firefox and Google Chrome.
- Display: built-in 15.6-inch display, 2560 x 1440 pixels, 165 Hz.
- Requested camera constraints: `getUserMedia` ideal 640 x 480 pixels, ideal
  30 fps.
- Data output: CSV files packaged in a ZIP archive using JSZip.

## Environment

- Laboratory: indoor university laboratory/research room.
- Home: indoor private home room.
- Sessions were conducted during daytime in both contexts.
- Both rooms had windows and closed curtains.
- Both contexts used general indoor artificial lighting.
- Direct natural light was not the primary illumination source.
- Screen brightness was fixed across sessions.
- Brightness is reported as camera-derived brightness, not external lux.
- Camera-derived brightness range: laboratory 105--114, home 102--111.

## Task / Threshold

- Task: two-alternative forced-choice Gabor orientation discrimination.
- Orientations: -45 degrees and +45 degrees.
- Stimulus duration: 200 ms.
- Fixation duration: randomized 400--600 ms.
- Response mapping: F = -45 degrees, J = +45 degrees.
- Staircase: standard 1-up 1-down, relative +/-5% contrast steps.
- Face-tracking threshold: `Conf < 0.8` is an operational FaceMesh exclusion
  threshold, not an rPPG-quality validation threshold.
