# RQ1 Behavioral/Facial Alignment Audit

## Outcome

The final RQ1 trial percentage is **not computable from the available code and exported logs**.
The 541/600 value is reproducible for the RT condition alone, but it cannot be reused as the conjunctive RQ1 result because explicit stimulus-onset and response timestamps were not exported.
The zero count in the `alignment_verified` column below means zero trials were *verifiable from the required fields*; it is not an observed 0% alignment-performance result.

## Evidence from the implementation

- `TaskEngine.runTrial()` stores `startTime = performance.now()` before the 500 ms fixation period.
- It later creates `stimStart = performance.now()` after drawing the stimulus, but `stimStart` is not copied into the logged trial result.
- Reaction time is stored only as the duration `performance.now() - stimStart`.
- The actual response timestamp is not copied into the logged trial result.
- `DataLogger.logFrameFeatures()` stores facial-record timestamps as `t = performance.now()`.
- `trials.csv` contains `startTime` and `rt`, but no explicit stimulus-onset or response-timestamp field.
- No task-event log file exists in any of the ten session folders.
- Consequently, task and facial values use millisecond-scale browser timestamps, but the exact stimulus-to-response interval cannot be reconstructed without assuming nominal timer durations.
- The script does not use `startTime + 500`, neighboring trial times, or block times as substitutes, because those would be inferred rather than recorded event timestamps.

## Completed-trial definition used for this audit

A completed trial is a `trials.csv` row with a non-empty normalized response and a numeric RT. This follows the current code path: `TaskEngine` logs a trial result only after `waitForResponse()` resolves. All present trial rows meet this row-level definition.

The exported `response` field stores `LEFT` or `RIGHT`, not the physical input event. The code maps F to LEFT and J to RIGHT but also accepts left/right canvas clicks. Therefore the audit CSV reports `F_or_left_click` and `J_or_right_click`; the logs alone cannot verify which input method was used.

## Counts

| Scope | Completed trial rows | RT 100--1500 ms | Alignment verifiable | Both conditions verifiable |
|---|---:|---:|---:|---:|
| Total | 600 | 541 (90.2%) | 0 | 0 |
| Laboratory | 300 | 256 (85.3%) | 0 | 0 |
| Home | 300 | 285 (95.0%) | 0 | 0 |

## Per-session counts

| Folder | Metadata session ID | Setting | Completed rows | RT-qualified | Facial rows | Alignment verifiable | Both verifiable |
|---|---|---|---:|---:|---:|---:|---:|
| `data1` | `a231c6cf-61a4-4480-a394-dfbb705c3441` | Laboratory | 60 | 52 | 7095 | 0 | 0 |
| `data2` | `45f6e5c7-6868-44dd-b300-fe5f48daa7c8` | Laboratory | 60 | 51 | 6085 | 0 | 0 |
| `data3` | `45f6e5c7-6868-44dd-b300-fe5f48daa7c8` | Laboratory | 60 | 51 | 6085 | 0 | 0 |
| `data4` | `68f43e24-f6d2-4326-a310-ec8db5fba26d` | Laboratory | 60 | 51 | 6423 | 0 | 0 |
| `data5` | `57432c26-5632-4f67-9045-71f88e3574c8` | Laboratory | 60 | 51 | 7322 | 0 | 0 |
| `data6` | `6e4a132e-5079-492d-850b-befb3d25aa43` | Home | 60 | 55 | 7887 | 0 | 0 |
| `data7` | `3305cebf-0693-4333-a997-18495f64f80b` | Home | 60 | 59 | 7110 | 0 | 0 |
| `data8` | `7bbbc1ef-74dd-4161-88e4-3c5461283867` | Home | 60 | 57 | 6931 | 0 | 0 |
| `data9` | `b6c866de-56b3-4a83-8639-56e86de434dd` | Home | 60 | 58 | 7070 | 0 | 0 |
| `data10` | `82101231-c97f-4f8d-949e-852fe85195d6` | Home | 60 | 56 | 6837 | 0 | 0 |

## Duplicate-export audit

- `blocks.csv` is byte-identical in `data2`, `data3` (SHA-256 `49f7daedb22e4fc8868692bf59b48b96be7d9319155560257876e2ba43786d1e`).
- `features_raw.csv` is byte-identical in `data2`, `data3` (SHA-256 `99611c264bfbb014b5b34bef2c9666fb5ef2de205cbf0ec7f1d665804d9b6935`).
- `metadata.json` is byte-identical in `data2`, `data3` (SHA-256 `2c0b30596824a29a18bd95522f74cd49f65ad8749d2102ceb5ad4ffc7bcd6d41`).
- `trials.csv` is byte-identical in `data2`, `data3`, `data5` (SHA-256 `f446aa4ca46e1121dffbd394ed5d291a700546822ae9fe07008737fe7e3b502d`).
- `windows.csv` is byte-identical in `data2`, `data3` (SHA-256 `5720d77b3e765d31301db6f2761b732a353bc947079558fa7e3576b8f8a1b4b5`).
- Metadata session ID `45f6e5c7-6868-44dd-b300-fe5f48daa7c8` occurs in `data2`, `data3`.

These duplicates mean that the repository contains 600 trial rows across ten folders, but the available files do not establish ten unique session exports or 600 unique trial records.

## Missing information required to finish the requested RQ1 revision

1. The original explicit stimulus-onset timestamp for every trial.
2. The original explicit F/J key-response timestamp for every trial.
3. A task-event log or another documented mapping that places those timestamps on the same `performance.now()` session timeline as `features_raw.csv:t`.
4. The nonduplicated original exports for `data3`, and the correct original `trials.csv` for `data5`, or a documented explanation showing why those byte-identical files represent distinct observations.
5. If F/J responses must be verified from data, an input-method/key field; the current normalized LEFT/RIGHT field cannot distinguish keyboard responses from canvas clicks.

## Files audited

For each of `src/assets/data1` through `src/assets/data10`: `trials.csv`, `features_raw.csv`, `windows.csv`, `blocks.csv`, and `metadata.json`. The audit also inspected `TaskEngine.js`, `CameraManager.js`, `FeatureExtractor.js`, `DataLogger.js`, `SessionManager.js`, and `main.js`, as well as Git history for the task and logger implementations.

## Consequence for manuscript editing

Do not state that 541/600 trials satisfied both RQ1 conditions. Do not state that the new 80% conjunctive RQ1 criterion was met. The 541/600 (90.2%) value currently supports only the RT-range component, subject also to resolution of the duplicated session exports.
