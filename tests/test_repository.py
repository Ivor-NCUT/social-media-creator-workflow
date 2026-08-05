"""
[INPUT]: Repository project.json, skills, evals, knowledge, and routing cases.
[OUTPUT]: Structural and routing-fixture assertions runnable with Python stdlib.
[POS]: Repository-level regression checks; domain behavior remains in skill evals.
[PROTOCOL]: Update this test when expert count, naming, or installation shape changes.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
PROJECT = json.loads((ROOT / "project.json").read_text(encoding="utf-8"))
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


class RepositoryTest(unittest.TestCase):
    def test_expected_expert_count_and_names(self) -> None:
        experts = PROJECT["experts"]
        self.assertEqual(len(experts), 22)
        ids = [expert["id"] for expert in experts]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(SKILL_NAME_RE.fullmatch(expert_id) for expert_id in ids))

    def test_every_skill_has_grounded_pack_and_evals(self) -> None:
        project_name = PROJECT["project_name"]
        skill_names = [project_name] + [
            f"{project_name}-{expert['id']}" for expert in PROJECT["experts"]
        ]
        for skill_name in skill_names:
            skill_root = ROOT / "skills" / skill_name
            self.assertTrue((skill_root / "SKILL.md").is_file(), skill_name)
            eval_path = skill_root / "evals" / "evals.json"
            payload = json.loads(eval_path.read_text(encoding="utf-8"))
            self.assertEqual(payload["skill_name"], skill_name)
            self.assertGreaterEqual(len(payload["evals"]), 2)
        for expert in PROJECT["experts"]:
            pack = ROOT / "knowledge" / "skill-packs" / f"{expert['id']}.md"
            self.assertTrue(pack.is_file(), expert["id"])

    def test_no_source_grounding_todos_remain(self) -> None:
        marker = "TODO" + "(source-grounding)"
        for path in ROOT.rglob("*"):
            if not path.is_file() or ".git" in path.parts or "dist" in path.parts:
                continue
            if path.suffix not in {".md", ".json", ".jsonl", ".py"}:
                continue
            text = path.read_text(encoding="utf-8")
            self.assertNotIn(marker, text, str(path))

    def test_direct_routing_cases_are_covered_by_triggers(self) -> None:
        cases = json.loads((ROOT / "tests" / "routing_cases.json").read_text(encoding="utf-8"))
        experts = {expert["id"]: expert for expert in PROJECT["experts"]}
        self.assertEqual({case["expected"] for case in cases}, set(experts))
        for case in cases:
            triggers = experts[case["expected"]]["triggers"]
            self.assertTrue(
                any(trigger.lower() in case["prompt"].lower() for trigger in triggers),
                case,
            )

    def test_creator_buddy_capabilities_have_conflict_decisions(self) -> None:
        cases = json.loads(
            (ROOT / "tests" / "xhs_integration_cases.json").read_text(encoding="utf-8")
        )
        experts = {expert["id"] for expert in PROJECT["experts"]}
        self.assertEqual(len(cases), 10)
        self.assertEqual(len({case["source_family"] for case in cases}), 10)
        self.assertTrue(
            all(case["expected"] in experts or case["expected"] == "router" for case in cases)
        )

    def test_new_upstreams_have_conflict_decisions(self) -> None:
        cases = json.loads(
            (ROOT / "tests" / "upstream_integration_cases.json").read_text(encoding="utf-8")
        )
        experts = {expert["id"] for expert in PROJECT["experts"]}
        self.assertEqual(len(cases), 8)
        self.assertEqual(len({case["source_family"] for case in cases}), 8)
        self.assertTrue(
            all(case["expected"] in experts or case["expected"] == "router" for case in cases)
        )


if __name__ == "__main__":
    unittest.main()
