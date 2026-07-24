#!/usr/bin/env python3
"""Validate a project-level router-and-experts skill repository."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_ROOT = ("README.md", "AGENTS.md", "VERSION", "LICENSE", "project.json")
TEXT_SUFFIXES = {".md", ".json", ".jsonl", ".py", ".yml", ".yaml"}
SOURCE_GROUNDING_MARKER = "TODO" + "(source-grounding)"


def validate_jsonl(path: Path, source_ids: set[str] | None = None) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"missing {path}"]
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}:{number}: invalid JSON: {exc.msg}")
            continue
        if not isinstance(item, dict):
            errors.append(f"{path}:{number}: entry must be an object")
            continue
        if source_ids is not None:
            refs = item.get("source_ids", [])
            if not isinstance(refs, list) or any(ref not in source_ids for ref in refs):
                errors.append(f"{path}:{number}: unknown or invalid source_ids")
    return errors


def validate_project(root: Path) -> list[str]:
    errors: list[str] = []
    for name in REQUIRED_ROOT:
        if not (root / name).is_file():
            errors.append(f"missing root file: {name}")

    project_path = root / "project.json"
    if not project_path.is_file():
        return errors
    try:
        project = json.loads(project_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return errors + [f"project.json is invalid: {exc}"]

    name = project.get("project_name", "")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name):
        errors.append("project_name must use lowercase kebab-case")
        return errors

    experts = project.get("experts", [])
    if not isinstance(experts, list) or len(experts) < 2:
        errors.append("project.json must contain at least two experts")
        experts = []

    expected = [name] + [f"{name}-{item.get('id', '')}" for item in experts if isinstance(item, dict)]
    for skill_name in expected:
        skill_root = root / "skills" / skill_name
        skill_file = skill_root / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing skill: {skill_name}")
            continue
        text = skill_file.read_text(encoding="utf-8")
        if f"name: {skill_name}" not in text:
            errors.append(f"{skill_file}: frontmatter name mismatch")
        eval_path = skill_root / "evals" / "evals.json"
        if not eval_path.is_file():
            errors.append(f"missing evals: {skill_name}")
        else:
            try:
                eval_payload = json.loads(eval_path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"{eval_path}: invalid JSON: {exc}")
            else:
                if eval_payload.get("skill_name") != skill_name:
                    errors.append(f"{eval_path}: skill_name mismatch")
                evals = eval_payload.get("evals")
                if not isinstance(evals, list) or len(evals) < 2:
                    errors.append(f"{eval_path}: expected at least two evals")

    source_path = root / "knowledge" / "sources.jsonl"
    errors.extend(validate_jsonl(source_path))
    source_ids: set[str] = set()
    if source_path.exists():
        for line in source_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    item = json.loads(line)
                except json.JSONDecodeError:
                    continue
                source_id = item.get("id")
                if isinstance(source_id, str):
                    if source_id in source_ids:
                        errors.append(f"duplicate source id: {source_id}")
                    source_ids.add(source_id)

    errors.extend(validate_jsonl(root / "knowledge" / "atoms" / "atoms.jsonl", source_ids))
    errors.extend(validate_jsonl(root / "knowledge" / "cases" / "cases.jsonl", source_ids))

    for expert in experts:
        if not isinstance(expert, dict):
            continue
        expert_id = expert.get("id", "")
        pack = root / "knowledge" / "skill-packs" / f"{expert_id}.md"
        if not pack.is_file():
            errors.append(f"missing skill pack: {expert_id}")

    for relative in ("knowledge/glossary.md", "docs/architecture.md", "tools/validate_project.py"):
        if not (root / relative).is_file():
            errors.append(f"missing project component: {relative}")

    version_path = root / "VERSION"
    if version_path.is_file():
        version = version_path.read_text(encoding="utf-8").strip()
        if not re.fullmatch(r"\d+\.\d+\.\d+", version):
            errors.append("VERSION must use semantic versioning")

    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "dist" in path.parts:
            continue
        if path.suffix not in TEXT_SUFFIXES:
            continue
        if SOURCE_GROUNDING_MARKER in path.read_text(encoding="utf-8"):
            errors.append(f"{path}: unresolved source-grounding marker")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    args = parser.parse_args()
    root = args.project.resolve()
    errors = validate_project(root)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"VALID: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
