# Social Media Creator Workflow

A creator-first MOE skill system for moving social media content from topic selection to reusable content assets.

## Start

Invoke `/social-media-creator-workflow` and describe the real task. The main skill
selects one specialist from the current context.

## Experts

| Skill | Responsibility |
|---|---|
| `social-media-creator-workflow-topic-selector` | Turn creator context, audience needs, platform signals, and content goals into prioritized topics. |
| `social-media-creator-workflow-outline-builder` | Turn an accepted topic into a shootable and writable content outline with multiple opening options. |
| `social-media-creator-workflow-scene-designer` | Translate an outline into scenes, shots, props, actions, and visual information. |
| `social-media-creator-workflow-shooting-director` | Guide the creator through capturing complete, usable, and expressive footage. |
| `social-media-creator-workflow-content-writer` | Turn topics, outlines, and footage notes into scripts, narration, posts, or publishable articles. |
| `social-media-creator-workflow-rough-cut-planner` | Build the first coherent edit from raw footage while preserving the story and identifying missing material. |
| `social-media-creator-workflow-fine-cut-planner` | Specify pacing, captions, music, visual packaging, and export requirements after the rough cut is stable. |
| `social-media-creator-workflow-content-reviewer` | Review a finished or near-finished content piece and route revisions to the correct production stage. |
| `social-media-creator-workflow-multiplatform-distributor` | Adapt one content asset into platform-specific publishing packages without flattening platform differences. |
| `social-media-creator-workflow-data-organizer` | Normalize creator-provided screenshots or CSV exports into a comparable, auditable content dataset. |
| `social-media-creator-workflow-strategy-reviewer` | Turn normalized performance data into evidence-based content strategy and testable next actions. |
| `social-media-creator-workflow-asset-distiller` | Convert completed work and validated lessons into reusable creator assets with provenance and usage limits. |

## Repository

- `skills/`: main router and specialist workflows.
- `knowledge/`: sources, atoms, cases, glossary, and specialist skill packs.
- `docs/architecture.md`: responsibility and data-flow boundaries.
- `tools/validate_project.py`: structural validation.

## Validate

```bash
python3 tools/validate_project.py .
```

Before distribution, replace all `TODO(source-grounding)` markers with
evidence-backed domain instructions and review the license notice.
