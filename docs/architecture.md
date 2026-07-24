# Architecture

`social-media-creator-workflow` is the stable main entry point. It routes one current
task to one specialist:

- `social-media-creator-workflow-topic-selector`: Turn creator context, audience needs, platform signals, and content goals into prioritized topics.
- `social-media-creator-workflow-outline-builder`: Turn an accepted topic into a shootable and writable content outline with multiple opening options.
- `social-media-creator-workflow-scene-designer`: Translate an outline into scenes, shots, props, actions, and visual information.
- `social-media-creator-workflow-shooting-director`: Guide the creator through capturing complete, usable, and expressive footage.
- `social-media-creator-workflow-content-writer`: Turn topics, outlines, and footage notes into scripts, narration, posts, or publishable articles.
- `social-media-creator-workflow-rough-cut-planner`: Build the first coherent edit from raw footage while preserving the story and identifying missing material.
- `social-media-creator-workflow-fine-cut-planner`: Specify pacing, captions, music, visual packaging, and export requirements after the rough cut is stable.
- `social-media-creator-workflow-content-reviewer`: Review a finished or near-finished content piece and route revisions to the correct production stage.
- `social-media-creator-workflow-multiplatform-distributor`: Adapt one content asset into platform-specific publishing packages without flattening platform differences.
- `social-media-creator-workflow-data-organizer`: Normalize creator-provided screenshots or CSV exports into a comparable, auditable content dataset.
- `social-media-creator-workflow-strategy-reviewer`: Turn normalized performance data into evidence-based content strategy and testable next actions.
- `social-media-creator-workflow-asset-distiller`: Convert completed work and validated lessons into reusable creator assets with provenance and usage limits.

Shared knowledge lives outside the skills so specialists can evolve without
duplicating sources. `knowledge/sources.jsonl` is the provenance system of
record. Atoms and cases cite source IDs.

Routing is dynamic. A specialist result may suggest a possible next expert,
but the router re-evaluates from the latest context instead of enforcing a
fixed chain.
