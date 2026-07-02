# Author Facts Needed / Reporting Choices

No author-fill placeholders remain in the submission manuscript. Facts that were not recoverable from repository logs or explicit author input were reported conservatively as not logged or not systematically recorded.

## Hardware/software facts reported as unavailable

- Laptop/PC model: reported as `Not logged`.
- CPU: reported as `Not logged`.
- GPU: reported as `Not logged`.
- RAM: reported as `Not logged`.
- Exact OS build/version: reported as `not logged`; available metadata only supports Windows NT 10.0 from the Firefox user agent.
- Chrome deployment-time version: reported as not logged; author input states Chrome was used, but repository metadata available here records Firefox user agents.
- Webcam type/model: reported as `Not logged`.
- Actual camera resolution and actual camera frame rate: reported as not programmatically logged; the manuscript separately reports requested `getUserMedia` constraints and measured processing FPS.
- Auto-exposure and auto-white-balance: reported as device/browser default, exact deployment-time state not programmatically logged.

## Environment facts reported as unavailable

- Lux meter model: reported as `Not logged`.
- Lux measurement timing/window: reported as `Not systematically recorded`.
- Window presence, natural-light contribution, curtain/blind condition, weather, time of day, and screen brightness: reported as `Not systematically recorded`.
- Clouds, screen flicker, and power cycles: reported only as possible sources of luminance fluctuation, not as observed session events.

## FaceMesh confidence threshold

The `Conf < 0.8` threshold is reported as an operational exclusion threshold for low FaceMesh tracking confidence in the exploratory analysis. The manuscript states that it was not independently validated as an rPPG-quality threshold.
