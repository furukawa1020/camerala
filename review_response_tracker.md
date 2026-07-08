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
| 2 | Explain necessity of real-time processing | Clarify that real-time processing is not the only technically possible architecture; acknowledge offline local video processing could preserve timestamps, but argue that retaining identifiable facial video is a privacy and acceptability burden in private remote task experiments. Position real-time browser-side processing as feature-only local logging and timestamp alignment in the same client runtime, not online task adaptation or more accurate physiological estimates. | Quote new paragraph on offline processing possibility, raw-video persistence burden, feature-only local logging, and timestamp alignment. | Drafted |
| 3 | Clarify RQ1 and success criteria | Replace RQ1 with intended remote psychological/psychophysiological task-use-case wording; ask whether task-synchronized face-derived records, including rPPG-oriented ROI values, satisfy the operational criteria for descriptive analysis: trial-level RT within 100--1500 ms and exported-window-level landmark availability of `mean_quality >= 0.8`. | Quote revised RQ1, the trial/exported-window operational criteria, the 541/600 RT-retained trials, and the result that all 299 exported windows had `mean_quality = 1.0`. | Drafted |
| 4 | Define "between-environment differences" in RQ2 | Retain the original intent of RQ2, but clarify immediately after it that "physiological signals" is used operationally to refer to task-synchronized face-derived and sensor-derived exported records, including rPPG-oriented ROI values and related exported fields, not validated physiological-state measurements. Keep the Lab/Home comparison, but state that the differences may reflect lighting, screen light, posture, camera geometry, task timing, measurement-pipeline factors, participant state, or their mixture, and are interpreted as deployment-context differences rather than psychological/physiological effects. | Quote the retained RQ2 and the operational definition / deployment-context interpretation paragraph. | Drafted |
| 5 | Justify novelty and positioning | Include all reviewer-specified related studies/systems: Gupta and Etemad, Ayesha et al., LabVanced rPPG, FacePhys-Demo, RhythmEdge, and Di Lernia et al.; treat LabVanced/FacePhys-Demo as public tools/demonstrations; use OA peer-reviewed papers only as supporting context. Do not claim novelty in browser rPPG, local rPPG processing, edge-based heart-rate estimation, or privacy preservation as an algorithm. Position Camerala as a limited system-integration implementation / system-development contribution for remote psychological/psychophysiological task experiments: task execution + face-derived feature extraction + task-event/frame-record timestamp alignment + operational landmark-availability checking + local CSV/ZIP persistence without raw facial video retention. | Explicitly list all six reviewer-specified items; explain LabVanced/FacePhys-Demo are public tools/demos, not peer-reviewed empirical studies; quote system-integration positioning paragraph. | Drafted; all reviewer-specified items retained in manuscript and references |
| 6 | Clarify rigid head-motion robustness claim | Remove unsupported computational-efficiency and rigid-head-motion-robustness claims; present Camerala as a deployment/logging architecture, not a method for improving rPPG signal quality under motion. Retain motion estimates only as task-synchronized face-derived exported records for descriptive inspection, and state that they do not correct or demonstrate correction of motion-induced rPPG degradation. | Quote the revised Feature Extraction, Results, Discussion, and Limitations wording. | Drafted |
| 7 | Clarify concrete usage scenario | Define Camerala's target use case as a browser-based remote psychological/psychophysiological task experiment conducted in laboratory and home settings. State plainly that the participant sits in front of a laptop, views task stimuli, and responds by key press, and that Camerala is not intended for continuous physiological sensing during ordinary daily activities. | Quote the revised Introduction and Methodology usage-scenario paragraphs. | Drafted |
| 8 | Define/qualify "in-the-wild" and "naturalistic" | Remove unqualified "in-the-wild" and "naturalistic" expressions; describe the study as a browser-based remote psychological/psychophysiological task experiment conducted in laboratory and home settings. Distinguish the seated Gabor-stimulus/key-press task from unconstrained daily-life physiological sensing during walking, conversation, cooking, sleep, or other ordinary activities. | Show risky-term search and quote revised scope statement. | Drafted |
| 9 | Add hardware/software reproducibility details | Add hardware/software table with author-confirmed PC model, CPU/GPU, RAM, storage, OS, display, browser names, built-in webcam, getUserMedia constraints, fixed screen brightness, and camera-control behavior. Explicitly mark unlogged deployment-time details, including exact OS/browser versions when unavailable, actual negotiated camera resolution/frame rate, exact internal webcam model, and auto-exposure/auto-white-balance states. | Quote Table 2 statement that unlogged values are marked as not logged rather than inferred from the revision-time environment. | Drafted |
| 10 | Add experimental environment details | Replace lux-based description with camera-derived brightness, daytime sessions, room type, windows, closed curtains, artificial lighting, fixed screen brightness, and aggregation details. | Quote/table reference and state lux values were removed. | Drafted |
| 11 | Reposition cognitive framing manipulation | Replace cognitive/motivational manipulation claims with exploratory instructional/task-interface contexts. State that negative/neutral/positive contexts demonstrate synchronized logging across instruction frames, not validated induction of evaluation pressure, reward motivation, cognitive state, motivational state, psychological effects, or motivational effects; note author-participant knowledge and lack of manipulation check. | Quote revised Methodology, Results, and Discussion/Limitation paragraphs. | Drafted |
| 12 | Reconsider central Discussion claim | Shift Discussion from "lab-only validation overestimates..." to design requirements and safeguards for future Camerala deployments. | Quote revised Discussion topic sentences and safeguards. | Drafted |
| 13 | Weaken unsupported claims | Replace "establishes"; weaken feasibility/naturalistic claims; clarify that `quality` is a binary landmark-availability flag and `mean_quality` is its 10-s exported-window average, not a continuous MediaPipe confidence score, all-camera-frame face-detection availability, or an indicator of rPPG measurement quality. Revise Abstract and Conclusion accordingly. | Quote revised Abstract/Conclusion/Limitations and the `mean_quality` explanation; state that all 299 exported windows met the 0.8 operational landmark-availability criterion. | Drafted |

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
