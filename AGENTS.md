# Project instructions

## Product boundary

- Preserve the thin main-router/specialist boundary.
- One specialist owns one current creator outcome.
- Users may enter at any stage; never force the full workflow.
- Ground domain claims in `knowledge/sources.jsonl`.
- Keep time-sensitive platform claims dated and uncertain.
- Do not copy long passages from source materials.

## Change protocol

When adding, removing, or renaming an expert, update:

1. `project.json`
2. `skills/social-media-creator-workflow/SKILL.md`
3. the expert Skill and `knowledge/skill-packs/<expert>.md`
4. `docs/architecture.md`
5. the expert eval file and routing cases

Run before commit:

```bash
python3 tools/validate_project.py .
python3 -m unittest discover -s tests -v
python3 -m unittest discover \
  -s skills/social-media-creator-workflow-data-organizer/tests -v
```

Keep the repository installable as one directory because specialists read shared knowledge by
relative path.
