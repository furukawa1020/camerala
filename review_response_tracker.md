# Review Response Tracker

Working manuscript: `paper_his_revision.tex`

Protected submitted manuscript: `paper_his.tex` and `paper_his.pdf`

This tracker exists so that every required condition can later be answered in a
one-question-one-answer response letter. Do not mark a condition as complete
until the manuscript edit and the response text both exist.

## Required Conditions

| No. | Reviewer 1 condition | Manuscript response needed | Response-letter evidence | Status |
| --- | --- | --- | --- | --- |
| 1 | Reconsider title | Remove title-level "Privacy-Preserving"; use a modest browser-native/task-aligned title. | Quote old/new title and explain that privacy is framed as local-first architecture, not a dedicated privacy method. | Drafted |
| 2 | Explain necessity of real-time processing | Add early explanation that real-time processing avoids raw-video persistence, supports same-runtime task/frame synchronization, and enables quality flags; acknowledge offline local video processing is possible. | Quote new paragraph on real-time processing and local-first feature logging. | Drafted |
| 3 | Clarify RQ1 and success criteria | Replace RQ1 with tested-configuration wording; define completion, local persistence, synchronized logs, retention after criteria, and availability of quality indicators. | Quote revised RQ1 and success/observation criteria. | Drafted |
| 4 | Define "between-environment differences" in RQ2 | Reframe RQ2 as descriptive differences in measurement-quality indicators and sensor-derived estimates, not psychological/physiological effects. | Quote revised RQ2 and interpretive caution. | Drafted |
| 5 | Justify novelty and positioning | Discuss prior web/edge/privacy-oriented rPPG systems and public tools; explicitly state novelty is integrated task execution + on-device features + timestamped local logging, not browser rPPG or local rPPG alone. | List added related systems and quote positioning paragraph. | Drafted; MediaPipe arXiv used only as a technical implementation reference |
| 6 | Clarify rigid head-motion robustness claim | Remove robustness claim or convert to quality-aware logging; state Camerala records motion/luminance indicators but does not correct rPPG degradation. | Quote revised wording replacing robustness. | Drafted |
| 7 | Clarify concrete usage scenario | State target use case: seated, task-constrained, home/lab psychophysical experiments with browser-based behavioral and webcam-derived feature logging. | Quote new usage-scenario paragraph. | Drafted |
| 8 | Define/qualify "in-the-wild" and "naturalistic" | Replace unqualified terms with task-constrained home/lab deployment; avoid implying unconstrained daily-life sensing. | Show risky-term search and quote revised scope statement. | Drafted |
| 9 | Add hardware/software reproducibility details | Add hardware/software table with PC, CPU/GPU, RAM, storage, OS, browser, built-in webcam, requested constraints, display refresh, fixed screen brightness, auto-exposure, and auto-white-balance. | Quote/table reference. | Drafted |
| 10 | Add experimental environment details | Replace lux-based description with camera-derived brightness, daytime sessions, room type, windows, closed curtains, artificial lighting, fixed screen brightness, and aggregation details. | Quote/table reference and state lux values were removed. | Drafted |
| 11 | Reposition cognitive framing manipulation | Replace cognitive/motivational interpretation with "instructional task contexts"; state author-participant knowledge prevents claims about induced pressure/reward. | Quote revised participant/framing paragraph. | Drafted |
| 12 | Reconsider central Discussion claim | Shift Discussion from "lab-only validation overestimates..." to design requirements and safeguards for future Camerala deployments. | Quote revised Discussion topic sentences and safeguards. | Drafted |
| 13 | Weaken unsupported claims | Replace "establishes"; weaken feasibility/naturalistic claims; clarify confidence threshold, tracking confidence limitations, and scope of findings. Revise Abstract and Conclusion accordingly. | Quote revised Abstract/Conclusion/Limitations and confidence-threshold explanation. | Drafted |

## Reviewer 1 Other Comments

| Item | Needed action | Status |
| --- | --- | --- |
| Table 1 readability | Increase readability and/or simplify table layout. | Drafted |
| Figure 2 readability and explanation | Remove old overclaiming figure from revised manuscript and rely on conservative table/text. | Drafted |
| Figure 4 readability | Remove old overclaiming longitudinal figure from revised manuscript and rely on conservative text. | Drafted |
| Figure 3 caption inconsistency | Remove old overclaiming task-result figure from revised manuscript. | Drafted |

## Response Letter Rule

For each condition in `response_to_reviewers.tex`, fill:

1. Response
2. Revision
3. Key revised manuscript text
4. Location

Do not leave TODO placeholders in the final manuscript or response letter.
