---
name: social-media-creator-workflow
description: |
  A creator-first MOE skill system for moving social media content from topic selection to reusable content assets.
---

# Social Media Creator Workflow

This is the main router. Read the current conversation first, select one
specialist for the current task, and explain the handoff in one sentence.

## Expert map

| Expert | Skill | Owned job | Trigger signals |
|---|---|---|---|
| Creator Topic Selector | `social-media-creator-workflow-topic-selector` | Turn creator context, audience needs, platform signals, and content goals into prioritized topics. | 定选题、选题规划、下一条拍什么、内容选题 |
| Creator Outline Builder | `social-media-creator-workflow-outline-builder` | Turn an accepted topic into a shootable and writable content outline with multiple opening options. | 出提纲、内容结构、视频大纲、多个开头 |
| Creator Scene Designer | `social-media-creator-workflow-scene-designer` | Translate an outline into scenes, shots, props, actions, and visual information. | 布场景、镜头设计、拍摄场景、分镜 |
| Creator Shooting Director | `social-media-creator-workflow-shooting-director` | Guide the creator through capturing complete, usable, and expressive footage. | 引导拍摄、拍摄指导、补拍清单、怎么拍 |
| Creator Content Writer | `social-media-creator-workflow-content-writer` | Turn topics, outlines, and footage notes into scripts, narration, posts, or publishable articles. | 出文章、写口播稿、写旁白、写图文 |
| Creator Rough Cut Planner | `social-media-creator-workflow-rough-cut-planner` | Build the first coherent edit from raw footage while preserving the story and identifying missing material. | 粗剪、素材筛选、粗剪时间线、整理素材 |
| Creator Fine Cut Planner | `social-media-creator-workflow-fine-cut-planner` | Specify pacing, captions, music, visual packaging, and export requirements after the rough cut is stable. | 精剪、字幕包装、BGM设计、剪辑节奏 |
| Creator Content Reviewer | `social-media-creator-workflow-content-reviewer` | Review a finished or near-finished content piece and route revisions to the correct production stage. | 审片、内容审核、成片复查、发布前检查 |
| Creator Multiplatform Distributor | `social-media-creator-workflow-multiplatform-distributor` | Adapt one content asset into platform-specific publishing packages without flattening platform differences. | 多平台分发、一稿多发、小红书适配、平台发布 |
| Creator Data Organizer | `social-media-creator-workflow-data-organizer` | Normalize creator-provided screenshots or CSV exports into a comparable, auditable content dataset. | 数据整理、后台截图、CSV分析、运营数据清洗 |
| Creator Strategy Reviewer | `social-media-creator-workflow-strategy-reviewer` | Turn normalized performance data into evidence-based content strategy and testable next actions. | 策略复盘、运营建议、数据复盘、下一步怎么做 |
| Creator Asset Distiller | `social-media-creator-workflow-asset-distiller` | Convert completed work and validated lessons into reusable creator assets with provenance and usage limits. | 内容资产沉淀、方法复用、素材库、经验沉淀 |

## Routing workflow

1. Reuse goals, materials, constraints, and prior results already in context.
2. Select one specialist whose owned job matches the user's current outcome.
3. If two specialists remain equally plausible, ask one decisive question.
4. Execute that specialist's workflow; do not make the user repeat context.
5. Re-evaluate after the result if the user wants to continue.

## Boundaries

- Do not perform every specialist job inside this router.
- Do not prescribe a fixed expert chain in advance.
- Do not invent source-backed claims when the knowledge assets are incomplete.
- Read `knowledge/sources.jsonl` before using imported domain material.

## Source grounding

TODO(source-grounding): Add domain-specific routing examples supported by the
registered materials.
