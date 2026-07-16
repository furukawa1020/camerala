#!/usr/bin/env python3
"""Audit trial-level behavioral/facial temporal alignment for RQ1.

This script intentionally does not infer stimulus-onset or response timestamps
from trial start times, nominal fixation durations, neighboring trials, or block
timestamps.  RQ1 alignment is verified only when explicit event timestamps are
present in the exported trial/event records and corresponding facial records
can be identified on the same session timeline.
"""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parent
DATA_ROOT = ROOT / "src" / "assets"
OUTPUT_CSV = ROOT / "analysis_rq1_behavioral_facial_alignment.csv"
OUTPUT_MD = ROOT / "analysis_rq1_behavioral_facial_alignment.md"

SESSION_SETTINGS = {
    **{index: "Laboratory" for index in range(1, 6)},
    **{index: "Home" for index in range(6, 11)},
}

STIMULUS_ONSET_FIELDS = (
    "stimulus_onset_timestamp",
    "stimulusOnsetTimestamp",
    "stimulus_onset",
    "stimulusOnset",
    "stimStart",
    "stim_start",
)
RESPONSE_TIMESTAMP_FIELDS = (
    "response_timestamp",
    "responseTimestamp",
    "key_response_timestamp",
    "keyResponseTimestamp",
    "responseTime",
)

OUTPUT_FIELDS = (
    "session_id",
    "source_folder",
    "setting",
    "block_id",
    "trial_id",
    "condition",
    "stimulus_orientation",
    "response_key",
    "correct",
    "stimulus_onset_timestamp",
    "response_timestamp",
    "reaction_time_ms",
    "rt_between_100_and_1500",
    "trial_interval_start",
    "trial_interval_end",
    "temporal_alignment_verified",
    "corresponding_facial_record_count",
    "rq1_qualified_trial",
    "exclusion_reason",
)


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader), list(reader.fieldnames or [])


def parse_float(value: Any) -> float | None:
    if value is None or str(value).strip() == "":
        return None
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def parse_bool(value: Any) -> bool | None:
    if value is None:
        return None
    normalized = str(value).strip().lower()
    if normalized in {"true", "1", "yes"}:
        return True
    if normalized in {"false", "0", "no"}:
        return False
    return None


def first_numeric(row: dict[str, str], names: Iterable[str]) -> tuple[str | None, float | None]:
    for name in names:
        if name in row:
            parsed = parse_float(row.get(name))
            if parsed is not None:
                return name, parsed
    return None, None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def response_label(value: str) -> str:
    """Preserve the ambiguity created by normalized direction-only logging."""
    normalized = value.strip().upper()
    if normalized == "LEFT":
        return "F_or_left_click"
    if normalized == "RIGHT":
        return "J_or_right_click"
    return value


def pct(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "n/a"
    return f"{100.0 * numerator / denominator:.1f}%"


def main() -> None:
    audit_rows: list[dict[str, Any]] = []
    session_summaries: list[dict[str, Any]] = []
    file_hash_groups: dict[str, dict[str, list[str]]] = defaultdict(lambda: defaultdict(list))
    metadata_session_groups: dict[str, list[str]] = defaultdict(list)
    missing_event_files: list[str] = []

    for index, setting in SESSION_SETTINGS.items():
        folder_name = f"data{index}"
        folder = DATA_ROOT / folder_name
        required = {
            "trials.csv": folder / "trials.csv",
            "features_raw.csv": folder / "features_raw.csv",
            "windows.csv": folder / "windows.csv",
            "blocks.csv": folder / "blocks.csv",
            "metadata.json": folder / "metadata.json",
        }
        absent = [name for name, path in required.items() if not path.exists()]
        if absent:
            raise FileNotFoundError(f"{folder_name}: missing {', '.join(absent)}")

        trials, trial_fields = read_csv(required["trials.csv"])
        features, feature_fields = read_csv(required["features_raw.csv"])
        windows, _ = read_csv(required["windows.csv"])
        blocks, _ = read_csv(required["blocks.csv"])
        metadata = json.loads(required["metadata.json"].read_text(encoding="utf-8-sig"))

        session_id = str(metadata.get("sessionId", ""))
        metadata_session_groups[session_id].append(folder_name)
        for name, path in required.items():
            file_hash_groups[name][sha256(path)].append(folder_name)

        event_files = [
            path
            for path in folder.iterdir()
            if path.is_file() and "event" in path.name.lower()
        ]
        if not event_files:
            missing_event_files.append(folder_name)

        feature_timestamps = sorted(
            timestamp
            for timestamp in (parse_float(row.get("t")) for row in features)
            if timestamp is not None
        )

        completed_count = 0
        rt_qualified_count = 0
        alignment_verified_count = 0
        both_verified_count = 0
        onset_fields_seen: Counter[str] = Counter()
        response_fields_seen: Counter[str] = Counter()

        for trial in trials:
            response = str(trial.get("response", "")).strip()
            rt = parse_float(trial.get("rt"))

            # TaskEngine writes a trial row only after a response resolves.  For
            # the present exports, a completed row therefore requires both a
            # normalized response value and an RT value.
            completed = bool(response) and rt is not None
            if completed:
                completed_count += 1

            rt_qualified = completed and 100.0 <= rt <= 1500.0
            if rt_qualified:
                rt_qualified_count += 1

            onset_field, onset = first_numeric(trial, STIMULUS_ONSET_FIELDS)
            response_field, response_timestamp = first_numeric(trial, RESPONSE_TIMESTAMP_FIELDS)
            if onset_field:
                onset_fields_seen[onset_field] += 1
            if response_field:
                response_fields_seen[response_field] += 1

            facial_count: int | None = None
            temporal_alignment_verified: bool | None = None
            interval_start: float | None = None
            interval_end: float | None = None

            if onset is not None and response_timestamp is not None and response_timestamp >= onset:
                interval_start = onset
                interval_end = response_timestamp
                facial_count = sum(interval_start <= timestamp <= interval_end for timestamp in feature_timestamps)
                temporal_alignment_verified = facial_count > 0
                if temporal_alignment_verified:
                    alignment_verified_count += 1

            rq1_qualified: bool | None
            if temporal_alignment_verified is None:
                rq1_qualified = None
            else:
                rq1_qualified = bool(rt_qualified and temporal_alignment_verified)
                if rq1_qualified:
                    both_verified_count += 1

            if temporal_alignment_verified is None:
                exclusion_reason = (
                    "temporal_alignment_not_verified"
                    if rt_qualified
                    else "rt_and_alignment_failed"
                )
            elif not rt_qualified and not temporal_alignment_verified:
                exclusion_reason = "rt_and_alignment_failed"
            elif rt is None:
                exclusion_reason = "missing_response_timestamp"
            elif rt < 100.0:
                exclusion_reason = "rt_below_100_ms"
            elif rt > 1500.0:
                exclusion_reason = "rt_above_1500_ms"
            elif facial_count == 0:
                exclusion_reason = "no_corresponding_facial_record"
            else:
                exclusion_reason = "none"

            audit_rows.append(
                {
                    "session_id": session_id,
                    "source_folder": folder_name,
                    "setting": setting,
                    "block_id": trial.get("blockId", ""),
                    "trial_id": trial.get("id", ""),
                    "condition": trial.get("condition", ""),
                    "stimulus_orientation": trial.get("stimulus", ""),
                    "response_key": response_label(response),
                    "correct": parse_bool(trial.get("correct")),
                    "stimulus_onset_timestamp": "" if onset is None else onset,
                    "response_timestamp": "" if response_timestamp is None else response_timestamp,
                    "reaction_time_ms": "" if rt is None else rt,
                    "rt_between_100_and_1500": rt_qualified,
                    "trial_interval_start": "" if interval_start is None else interval_start,
                    "trial_interval_end": "" if interval_end is None else interval_end,
                    "temporal_alignment_verified": (
                        "not_verifiable"
                        if temporal_alignment_verified is None
                        else temporal_alignment_verified
                    ),
                    "corresponding_facial_record_count": (
                        "" if facial_count is None else facial_count
                    ),
                    "rq1_qualified_trial": (
                        "not_verifiable" if rq1_qualified is None else rq1_qualified
                    ),
                    "exclusion_reason": exclusion_reason,
                }
            )

        session_summaries.append(
            {
                "folder": folder_name,
                "session_id": session_id,
                "setting": setting,
                "trial_rows": len(trials),
                "completed": completed_count,
                "rt_qualified": rt_qualified_count,
                "alignment_verified": alignment_verified_count,
                "both_verified": both_verified_count,
                "feature_rows": len(features),
                "window_rows": len(windows),
                "block_rows": len(blocks),
                "trial_fields": trial_fields,
                "feature_fields": feature_fields,
                "onset_fields_seen": dict(onset_fields_seen),
                "response_fields_seen": dict(response_fields_seen),
            }
        )

    with OUTPUT_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(audit_rows)

    total_completed = sum(item["completed"] for item in session_summaries)
    total_rt = sum(item["rt_qualified"] for item in session_summaries)
    total_alignment = sum(item["alignment_verified"] for item in session_summaries)
    total_both = sum(item["both_verified"] for item in session_summaries)
    any_explicit_event_timestamps = any(
        item["onset_fields_seen"] and item["response_fields_seen"]
        for item in session_summaries
    )

    setting_totals: dict[str, Counter[str]] = defaultdict(Counter)
    for item in session_summaries:
        setting_totals[item["setting"]].update(
            {
                "completed": item["completed"],
                "rt_qualified": item["rt_qualified"],
                "alignment_verified": item["alignment_verified"],
                "both_verified": item["both_verified"],
            }
        )

    duplicate_lines: list[str] = []
    for name, groups in sorted(file_hash_groups.items()):
        for digest, folders in sorted(groups.items()):
            if len(folders) > 1:
                duplicate_lines.append(
                    f"- `{name}` is byte-identical in {', '.join(f'`{folder}`' for folder in folders)} "
                    f"(SHA-256 `{digest}`)."
                )
    for session_id, folders in sorted(metadata_session_groups.items()):
        if session_id and len(folders) > 1:
            duplicate_lines.append(
                f"- Metadata session ID `{session_id}` occurs in "
                f"{', '.join(f'`{folder}`' for folder in folders)}."
            )

    lines = [
        "# RQ1 Behavioral/Facial Alignment Audit",
        "",
        "## Outcome",
        "",
    ]
    if any_explicit_event_timestamps:
        lines.extend(
            [
                f"The available exports contain explicit event timestamps. {total_both}/{total_completed} "
                f"completed trials ({pct(total_both, total_completed)}) were verifiably RQ1-qualified.",
                "",
            ]
        )
    else:
        lines.extend(
            [
                "The final RQ1 trial percentage is **not computable from the available code and exported logs**.",
                "The 541/600 value is reproducible for the RT condition alone, but it cannot be reused as the "
                "conjunctive RQ1 result because explicit stimulus-onset and response timestamps were not exported.",
                "The zero count in the `alignment_verified` column below means zero trials were *verifiable from "
                "the required fields*; it is not an observed 0% alignment-performance result.",
                "",
            ]
        )

    lines.extend(
        [
            "## Evidence from the implementation",
            "",
            "- `TaskEngine.runTrial()` stores `startTime = performance.now()` before the 500 ms fixation period.",
            "- It later creates `stimStart = performance.now()` after drawing the stimulus, but `stimStart` is not "
            "copied into the logged trial result.",
            "- Reaction time is stored only as the duration `performance.now() - stimStart`.",
            "- The actual response timestamp is not copied into the logged trial result.",
            "- `DataLogger.logFrameFeatures()` stores facial-record timestamps as `t = performance.now()`.",
            "- `trials.csv` contains `startTime` and `rt`, but no explicit stimulus-onset or response-timestamp field.",
            "- No task-event log file exists in any of the ten session folders.",
            "- Consequently, task and facial values use millisecond-scale browser timestamps, but the exact "
            "stimulus-to-response interval cannot be reconstructed without assuming nominal timer durations.",
            "- The script does not use `startTime + 500`, neighboring trial times, or block times as substitutes, "
            "because those would be inferred rather than recorded event timestamps.",
            "",
            "## Completed-trial definition used for this audit",
            "",
            "A completed trial is a `trials.csv` row with a non-empty normalized response and a numeric RT. "
            "This follows the current code path: `TaskEngine` logs a trial result only after `waitForResponse()` "
            "resolves. All present trial rows meet this row-level definition.",
            "",
            "The exported `response` field stores `LEFT` or `RIGHT`, not the physical input event. The code maps "
            "F to LEFT and J to RIGHT but also accepts left/right canvas clicks. Therefore the audit CSV reports "
            "`F_or_left_click` and `J_or_right_click`; the logs alone cannot verify which input method was used.",
            "",
            "## Counts",
            "",
            "| Scope | Completed trial rows | RT 100--1500 ms | Alignment verifiable | Both conditions verifiable |",
            "|---|---:|---:|---:|---:|",
            f"| Total | {total_completed} | {total_rt} ({pct(total_rt, total_completed)}) | "
            f"{total_alignment} | {total_both} |",
        ]
    )
    for setting in ("Laboratory", "Home"):
        counts = setting_totals[setting]
        lines.append(
            f"| {setting} | {counts['completed']} | {counts['rt_qualified']} "
            f"({pct(counts['rt_qualified'], counts['completed'])}) | "
            f"{counts['alignment_verified']} | {counts['both_verified']} |"
        )

    lines.extend(
        [
            "",
            "## Per-session counts",
            "",
            "| Folder | Metadata session ID | Setting | Completed rows | RT-qualified | Facial rows | "
            "Alignment verifiable | Both verifiable |",
            "|---|---|---|---:|---:|---:|---:|---:|",
        ]
    )
    for item in session_summaries:
        lines.append(
            f"| `{item['folder']}` | `{item['session_id']}` | {item['setting']} | "
            f"{item['completed']} | {item['rt_qualified']} | {item['feature_rows']} | "
            f"{item['alignment_verified']} | {item['both_verified']} |"
        )

    lines.extend(
        [
            "",
            "## Duplicate-export audit",
            "",
        ]
    )
    if duplicate_lines:
        lines.extend(duplicate_lines)
    else:
        lines.append("No byte-identical required exports or repeated metadata session IDs were found.")

    lines.extend(
        [
            "",
            "These duplicates mean that the repository contains 600 trial rows across ten folders, but the "
            "available files do not establish ten unique session exports or 600 unique trial records.",
            "",
            "## Missing information required to finish the requested RQ1 revision",
            "",
            "1. The original explicit stimulus-onset timestamp for every trial.",
            "2. The original explicit F/J key-response timestamp for every trial.",
            "3. A task-event log or another documented mapping that places those timestamps on the same "
            "`performance.now()` session timeline as `features_raw.csv:t`.",
            "4. The nonduplicated original exports for `data3`, and the correct original `trials.csv` for `data5`, "
            "or a documented explanation showing why those byte-identical files represent distinct observations.",
            "5. If F/J responses must be verified from data, an input-method/key field; the current normalized "
            "LEFT/RIGHT field cannot distinguish keyboard responses from canvas clicks.",
            "",
            "## Files audited",
            "",
            "For each of `src/assets/data1` through `src/assets/data10`: `trials.csv`, `features_raw.csv`, "
            "`windows.csv`, `blocks.csv`, and `metadata.json`. The audit also inspected `TaskEngine.js`, "
            "`CameraManager.js`, `FeatureExtractor.js`, `DataLogger.js`, `SessionManager.js`, and `main.js`, as well "
            "as Git history for the task and logger implementations.",
            "",
            "## Consequence for manuscript editing",
            "",
            "Do not state that 541/600 trials satisfied both RQ1 conditions. Do not state that the new 80% "
            "conjunctive RQ1 criterion was met. The 541/600 (90.2%) value currently supports only the RT-range "
            "component, subject also to resolution of the duplicated session exports.",
            "",
        ]
    )

    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUTPUT_CSV.name}: {len(audit_rows)} rows")
    print(f"Wrote {OUTPUT_MD.name}")
    print(f"Completed trial rows: {total_completed}")
    print(f"RT-qualified rows: {total_rt}")
    print("Final conjunctive RQ1 result: NOT COMPUTABLE")


if __name__ == "__main__":
    main()
