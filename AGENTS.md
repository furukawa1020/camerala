# AGENTS.md

This repository contains the LaTeX manuscript for Human Interface Society
Transactions paper S-28-4-002.

## Revision Target

Revise the manuscript for conditional acceptance.

- Reviewer 1: B, conditional acceptance
- Reviewer 2: A, acceptance
- Overall decision: B, conditional acceptance
- Required response: address Reviewer 1 Conditions 1--13

## Protected Files

Do not edit the submitted original manuscript files:

- `paper_his.tex`
- `paper_his.pdf`
- `paper_his_original_submitted.tex`
- `paper_his_original_submitted.pdf`

Use `paper_his_revision.tex` as the editable manuscript source.

## Core Revision Principle

Do not make the manuscript more ambitious. Make it more conservative, more
precise, and easier for the reviewer to accept.

The revised manuscript must not claim that Camerala is:

- a new rPPG estimator,
- a dedicated privacy-preserving algorithm,
- a general unconstrained in-the-wild physiological sensing system,
- evidence of psychological, cognitive, motivational, or physiological effects,
- generally feasible or robust across users, devices, and environments.

Instead, present Camerala as:

- a browser-native implementation example,
- a task-aligned physiological feature logging framework,
- a local-first architecture that avoids raw video transmission,
- a unified client-side runtime integrating psychophysical task execution,
  on-device rPPG/FaceMesh-derived feature extraction, frame-level quality
  indicators, and timestamped local persistence,
- evaluated only under limited, task-constrained home/laboratory conditions in
  an exploratory N=1 author-participant deployment.

## Safe Terminology

Prefer:

- "privacy-conscious" or "local-first" instead of "privacy-preserving"
- "architectural privacy advantage" instead of "privacy-preserving method"
- "rPPG-derived estimate" instead of "physiological signal" in Results
- "sensor-derived features" instead of "physiological effects"
- "measurement-quality indicators" instead of "environmental physiological differences"
- "task-constrained home/laboratory deployment" instead of unqualified
  "in-the-wild" or "naturalistic"
- "presents", "illustrates", or "provides an implementation example" instead
  of "establishes"
- "completed under the tested configuration" instead of broad "feasible"
- "quality-aware logging" instead of "robustness"

Avoid or remove unless strongly qualified:

- "Privacy-Preserving" in the title
- "establishes"
- "robust"
- "naturalistic physiological sensing"
- unqualified "in-the-wild physiological sensing"
- "physiological effects"
- "cognitive effects"
- "motivational effects"
- "general deployability"
- "general feasibility"
- "signal stability and condition separability" as a central claim

## No Fabrication Rule

Do not fabricate experimental facts. Do not invent hardware, software,
environmental, camera, lighting, weather, or measurement-protocol details.

If information is missing, insert a visible placeholder of the form:

`TODO_FURUKAWA_*`

Before finishing a revision pass, list all remaining `TODO_FURUKAWA_*`
placeholders for the author.

## Response Discipline

Every Reviewer 1 condition must be answerable one by one. Maintain:

- `review_response_tracker.md` for mapping conditions to manuscript edits,
- `response_to_reviewers.tex` for the final one-question-one-answer response.

For each condition, the final response should include:

- condition title,
- response,
- concrete revision,
- key revised text,
- manuscript location.

## Verification

Before final delivery, search the revised manuscript for risky terms:

- Privacy-Preserving
- establishes
- robust
- naturalistic
- in-the-wild
- physiological effects
- cognitive effects
- motivational effects
- feasible
- generalizable

For each remaining occurrence, remove it or ensure that it is strongly qualified.
