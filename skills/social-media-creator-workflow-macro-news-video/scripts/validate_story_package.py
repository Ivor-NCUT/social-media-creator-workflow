#!/usr/bin/env python3
"""Validate the evidence and artifact contract of a macro-news video job."""

from __future__ import annotations

import argparse
import json
import tempfile
from datetime import date
from pathlib import Path


BRIEF_FILES = (
    "source-ledger.json",
    "angle-brief.md",
    "script.md",
    "cover-brief.json",
    "storyboard.json",
)


def load_json(path: Path, errors: list[str]):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: {exc}")
        return None


def validate(root: Path, stage: str, min_duration: float) -> list[str]:
    errors: list[str] = []
    for name in BRIEF_FILES:
        path = root / name
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"missing or empty: {name}")

    ledger = load_json(root / "source-ledger.json", errors)
    claim_ids: set[str] = set()
    if isinstance(ledger, dict):
        try:
            date.fromisoformat(ledger["as_of"])
        except (KeyError, TypeError, ValueError):
            errors.append("source-ledger.json: as_of must be YYYY-MM-DD")
        claims = ledger.get("claims")
        if not isinstance(claims, list) or not claims:
            errors.append("source-ledger.json: claims must be a non-empty list")
        else:
            for claim in claims:
                if not isinstance(claim, dict) or not claim.get("id") or not claim.get("text"):
                    errors.append("source-ledger.json: each claim needs id and text")
                    continue
                claim_ids.add(claim["id"])
                if claim.get("used_in_script") and claim.get("status") != "verified":
                    errors.append(f"claim {claim['id']}: used claims must be verified")
                sources = claim.get("sources", [])
                urls = {source.get("url") for source in sources if isinstance(source, dict) and source.get("url")}
                primary = any(source.get("source_type") == "primary" for source in sources if isinstance(source, dict))
                if claim.get("used_in_script") and not (primary or len(urls) >= 2):
                    errors.append(f"claim {claim['id']}: needs a primary source or two independent URLs")

    cover = load_json(root / "cover-brief.json", errors)
    if isinstance(cover, dict):
        title = "".join(str(cover.get("main_title", "")).split())
        if not 6 <= len(title) <= 24:
            errors.append("cover-brief.json: main_title must contain 6-24 non-space characters")
        if not cover.get("subtitle") or not cover.get("visual_prompt"):
            errors.append("cover-brief.json: subtitle and visual_prompt are required")

    storyboard = load_json(root / "storyboard.json", errors)
    if isinstance(storyboard, dict):
        scenes = storyboard.get("scenes")
        if not isinstance(scenes, list) or len(scenes) < 3:
            errors.append("storyboard.json: at least three scenes are required")
        else:
            duration = 0.0
            for scene in scenes:
                missing = {"id", "duration", "narration", "visual", "evidence_ids", "transition"} - set(scene)
                if missing:
                    errors.append(f"storyboard scene missing: {', '.join(sorted(missing))}")
                    continue
                try:
                    duration += float(scene["duration"])
                except (TypeError, ValueError):
                    errors.append(f"scene {scene.get('id')}: duration must be numeric")
                unknown = set(scene.get("evidence_ids", [])) - claim_ids
                if unknown:
                    errors.append(f"scene {scene.get('id')}: unknown evidence ids {sorted(unknown)}")
            if duration < min_duration:
                errors.append(f"storyboard duration {duration:g}s is below {min_duration:g}s")

    if stage in {"composition", "final"}:
        for name in ("video/DESIGN.md", "video/index.html"):
            if not (root / name).is_file():
                errors.append(f"missing: {name}")
    if stage == "final":
        receipt = load_json(root / "video/listenhub-task.json", errors)
        if isinstance(receipt, dict):
            if receipt.get("status") != "success":
                errors.append("video/listenhub-task.json: status must be success")
            if not receipt.get("task_id") or not receipt.get("audio_url"):
                errors.append("video/listenhub-task.json: task_id and audio_url are required")
            try:
                if float(receipt.get("audio_duration", 0)) <= 0:
                    raise ValueError
            except (TypeError, ValueError):
                errors.append("video/listenhub-task.json: audio_duration must be positive")
        for name in ("video/final.mp4", "video/cover.png"):
            path = root / name
            if not path.is_file() or path.stat().st_size < 1024:
                errors.append(f"missing or implausibly small: {name}")
    return errors


def self_test() -> None:
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        (root / "angle-brief.md").write_text("大家看事件，我看成本转移。", encoding="utf-8")
        (root / "script.md").write_text("测试脚本", encoding="utf-8")
        (root / "source-ledger.json").write_text(json.dumps({
            "as_of": "2026-08-15",
            "claims": [{"id": "c1", "text": "测试事实", "status": "verified",
                        "used_in_script": True,
                        "sources": [{"url": "https://example.com/a", "source_type": "primary"}]}]}, ensure_ascii=False), encoding="utf-8")
        (root / "cover-brief.json").write_text(json.dumps({
            "main_title": "订单为什么突然变少", "subtitle": "需求才是关键",
            "visual_prompt": "dark factory"}, ensure_ascii=False), encoding="utf-8")
        scenes = [{"id": f"s{i}", "duration": 2, "narration": "测试", "visual": "数字卡",
                   "evidence_ids": ["c1"], "transition": "push"} for i in range(3)]
        (root / "storyboard.json").write_text(json.dumps({"scenes": scenes}, ensure_ascii=False), encoding="utf-8")
        assert validate(root, "brief", 6) == []
        assert validate(root, "brief", 7) == ["storyboard duration 6s is below 7s"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("job_dir", nargs="?", type=Path)
    parser.add_argument("--stage", choices=("brief", "composition", "final"), default="final")
    parser.add_argument("--min-duration", type=float, default=85)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        print("SELF-TEST OK")
        return 0
    if args.job_dir is None:
        parser.error("job_dir is required unless --self-test is used")
    errors = validate(args.job_dir.resolve(), args.stage, args.min_duration)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALID: {args.job_dir.resolve()} ({args.stage})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
