# Review Response Tracker

Working manuscript: `paper_his_revision.tex`

Final revised title: `Camerala: An Edge-Side, Browser-Native Framework for Remote Psychophysiological Experiments`

Final RQ1: `RQ1: Under the tested configuration, did Camerala complete all planned sessions and trials and export timestamped task-event and face-image-derived records using the same browser clock domain?`

Final RQ2: `RQ2: What between-environment differences are observable in the task-synchronized face-image-derived and sensor-derived exported records?`

Protected A1-submitted baseline: `paper_his_a1_submitted.tex` and `paper_his_a1_submitted.pdf`

Current A1 response: `response_to_a1_minor_revision.tex`

Current A1 difference manuscript: `paper_his_a1_minor_revision_diff.tex`

## A1 Administrative Inquiry

| No. | A1 item | Final action | Response evidence | Status |
| --- | --- | --- | --- | --- |
| Required 1 | Resolve task/display/illuminance contradictions | Six 10-trial blocks; G-Tune 15.6-inch 2560x1440 165-Hz display; no external illuminance measurement | `response_to_a1_minor_revision.tex`, Required Condition 1 | Complete |
| Required 2 | Remove `with rPPG Sensing` | Removed from title and current-output claims | Required Condition 2 | Complete |
| Required 3 | Remove percentage criterion from RQ1 | Replaced with planned-completion and same-browser-clock RQ; RT range retained only for descriptive preprocessing | Required Condition 3 | Complete |
| Required 4 | Replace `physiological signals` in RQ2 | RQ2 now names task-synchronized face-image-derived and sensor-derived exported records | Required Condition 4 | Complete |
| Required 5 | Define or remove setup brightness ranges | Removed 105--114 / 102--111 because provenance could not be reconstructed | Required Condition 5 | Complete |
| Required 6 | Remove `mean_quality = 1.0` result | Removed numeric result and retained one export-path limitation | Required Condition 6 | Complete |
| Other 1 | Reorganize Introduction | Rewritten as background, prior work/gap, Camerala purpose, and scope | Other Comment 1 | Complete |
| Other 2 | Add camera-setting future work | Added negotiated-resolution/frame-rate and camera-control logging requirement | Other Comment 2 | Complete |
| Other 3 | Remove revision meta-language | Removed revision-time wording from manuscript | Other Comment 3 | Complete |
| Other 4 | Reduce repeated negatives | Consolidated scope and limitations | Other Comment 4 | Complete |

The author portrait has been supplied as `古川耕太郎顔写真.jpg`, verified as a
731x981 JPEG, and copied to the submission name
`S-28-4-002_古川耕太郎_顔写真.jpg` in both the standalone deliverables and the
LaTeX source package.

This tracker exists so that every required condition can later be answered in a
one-question-one-answer response letter. Do not mark a condition as complete
until the manuscript edit and the response text both exist.

## July Conditional-Acceptance Conditions (Historical)

The following table records the earlier Reviewer 1 Conditions 1--13 addressed
in the July A1-submitted revision. The current A1 response above supersedes the
July response letter for the final submission.

| No. | Reviewer 1 condition | Manuscript response needed | Response-letter evidence | Status |
| --- | --- | --- | --- | --- |
| 1 | Reconsider title | Use the exact revised title `Camerala: An Edge-Side, Browser-Native Framework for Remote Psychophysiological Experiments with rPPG Sensing`; define edge-side as processing webcam frames in the participant's browser on the client device, and define rPPG sensing as acquisition/logging of facial ROI color traces for possible subsequent analysis. | Quote the exact revised title and explain that the prototype does not estimate validated heart rate, establish rPPG accuracy, or introduce a dedicated privacy-preserving method. | Drafted |
| 2 | Explain necessity of real-time processing | Clarify that real-time processing is not the only technically possible architecture; acknowledge offline local video processing could preserve timestamps, but argue that retaining identifiable facial video is a privacy and acceptability burden in private remote task experiments. Position real-time browser-side processing as feature-only local logging and timestamp alignment in the same client runtime, not online task adaptation or more accurate physiological estimates. | Quote new paragraph on offline processing possibility, raw-video persistence burden, feature-only local logging, and timestamp alignment. | Drafted |
| 3 | Clarify RQ1 and success criteria | Use the exact revised RQ1 above. Define a behavioral response as the participant's F/J response to Gabor orientation. Define the numerator as completed trials with stored RTs of 100--1500 ms inclusive and the denominator as all completed trials. Define temporally alignable form as exported trial/event and face-image-derived records carrying session-relative timestamps from the same browser clock domain; state that separate stimulus-onset and response timestamps were not exported. | Quote the exact RQ1, definitions, 541/600 (90.2%) RT result, exploratory 80% reference level, all-session temporally alignable export statement, exported timestamp fields, and the fact that the browser-side RT reference is captured immediately after the synchronous Canvas draw call returns while physical display onset remains unverified. State that 80% is not a face-detection rate, rPPG-quality threshold, or general feasibility standard, and do not claim exact face-frame matching to onset-to-response intervals. | Drafted |
| 4 | Define "between-environment differences" in RQ2 | Retain the original intent of RQ2, but clarify immediately after it that "physiological signals" is used operationally to refer to task-synchronized face-derived and sensor-derived exported records, including rPPG-oriented ROI values and related exported fields, not validated physiological-state measurements. Keep the Lab/Home comparison, but state that the differences may reflect lighting, screen light, posture, camera geometry, task timing, measurement-pipeline factors, participant state, or their mixture, and are interpreted as deployment-context differences rather than psychological/physiological effects. | Quote the retained RQ2 and the operational definition / deployment-context interpretation paragraph. | Drafted |
| 5 | Justify novelty and positioning | Include all reviewer-specified related studies/systems: Gupta and Etemad, Ayesha et al., LabVanced rPPG, FacePhys-Demo, RhythmEdge, and Di Lernia et al.; treat LabVanced/FacePhys-Demo as public tools/demonstrations; use OA peer-reviewed papers only as supporting context. Do not claim novelty in browser rPPG, local rPPG processing, edge-based heart-rate estimation, or privacy preservation as an algorithm. Position Camerala as a limited edge-side browser-native system-integration implementation / system-development contribution for remote psychological/psychophysiological task experiments: task execution + face-derived feature extraction + shared-clock session-relative timestamping of task and frame records + landmark-availability summaries for exported records + local CSV/ZIP persistence without raw facial video retention. | Explicitly list all six reviewer-specified items; explain LabVanced/FacePhys-Demo are public tools/demos, not peer-reviewed empirical studies; quote system-integration positioning paragraph. | Drafted; all reviewer-specified items retained in manuscript and references |
| 6 | Clarify rigid head-motion robustness claim | Remove unsupported computational-efficiency and rigid-head-motion-robustness claims; present Camerala as a deployment/logging architecture, not a method for improving rPPG signal quality under motion. Retain motion estimates only as task-synchronized face-derived exported records for descriptive inspection, and state that they do not correct or demonstrate correction of motion-induced rPPG degradation. | Quote the revised Feature Extraction, Results, Discussion, and Limitations wording. | Drafted |
| 7 | Clarify concrete usage scenario | Define Camerala's target use case as a browser-based remote psychological/psychophysiological task experiment conducted in laboratory and home settings. State plainly that the participant sits in front of a laptop, views task stimuli, and responds by key press, and that Camerala is not intended for continuous physiological sensing during ordinary daily activities. | Quote the revised Introduction and Methodology usage-scenario paragraphs. | Drafted |
| 8 | Define/qualify "in-the-wild" and "naturalistic" | Remove unqualified "in-the-wild" and "naturalistic" expressions; describe the study as a browser-based remote psychological/psychophysiological task experiment conducted in laboratory and home settings. Distinguish the seated Gabor-stimulus/key-press task from unconstrained daily-life physiological sensing during walking, conversation, cooking, sleep, or other ordinary activities. | Show risky-term search and quote revised scope statement. | Drafted |
| 9 | Add hardware/software reproducibility details | Add hardware/software table with author-confirmed PC model, CPU/GPU, RAM, storage, OS, display, browser names, built-in webcam, getUserMedia constraints, fixed screen brightness, and camera-control behavior. Explicitly mark unlogged deployment-time details, including exact OS/browser versions when unavailable, actual negotiated camera resolution/frame rate, exact internal webcam model, and auto-exposure/auto-white-balance states. | Quote Table 2 statement that unlogged values are marked as not logged rather than inferred from the revision-time environment. | Drafted |
| 10 | Add experimental environment details | Replace lux-based description with camera-derived brightness, daytime sessions, room type, windows, closed curtains, artificial lighting, fixed screen brightness, and aggregation details. | Quote/table reference and state lux values were removed. | Drafted |
| 11 | Reposition cognitive framing manipulation | Replace cognitive/motivational manipulation claims with exploratory instructional/task-interface contexts. State that negative/neutral/positive contexts demonstrate synchronized logging across instruction frames, not validated induction of evaluation pressure, reward motivation, cognitive state, motivational state, psychological effects, or motivational effects; note author-participant knowledge and lack of manipulation check. | Quote revised Methodology, Results, and Discussion/Limitation paragraphs. | Drafted |
| 12 | Reconsider central Discussion claim | Shift Discussion away from treating home/laboratory effects on camera-based physiological records as the central finding. State that this is a known limitation of video-based sensing, and position the contribution as design requirements and safeguards for an edge-side browser-native logging architecture: shared-clock session-relative timestamping of task and frame records, landmark-availability logging and its limitations, motion and brightness-change records, hardware/browser/camera reporting, environment reporting, and cautious interpretation without retained raw video. | Quote revised Discussion topic sentences and safeguards. | Drafted |
| 13 | Weaken unsupported claims | Revise Abstract, Discussion, and Conclusion so the paper supports only a limited implementation-level conclusion for this author-participant and tested device/environment/posture/lighting/task context. Remove or negate general feasibility, robustness, validity in other settings, validated rPPG accuracy, and psychological/physiological effect claims. Clarify that `mean_quality` is an exported-window-level landmark-availability summary, not MediaPipe confidence, rPPG quality, or primary evidence of successful deployment. | Quote the limited implementation-level conclusion; state that all 10 sessions and 600 trials were completed, 541/600 trials (90.2%) had RTs within the study-specific range, task-event and rPPG-sensing records were exported in a temporally alignable form for all sessions, and `mean_quality` is described only as a descriptive logging summary outside the main conclusion. | Drafted |

## Reviewer 1 Other Comments

| Item | Needed action | Status |
| --- | --- | --- |
| Table 1 readability | Increase readability and/or simplify table layout. | Drafted |
| Figure 2 readability and explanation | Remove old overclaiming figure from revised manuscript and rely on conservative table/text. | Drafted |
| Figure 4 readability | Remove old overclaiming longitudinal figure from revised manuscript and rely on conservative text. | Drafted |
| Figure 3 caption inconsistency | Remove old overclaiming task-result figure from revised manuscript. | Drafted |

## Response Letter Rule

For each item in `response_to_a1_minor_revision.tex`, include:

1. Comment
2. Response
3. Revision
4. Location

Do not leave TODO placeholders in the final manuscript or response letter.
