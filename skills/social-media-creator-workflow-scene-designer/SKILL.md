---
name: social-media-creator-workflow-scene-designer
description: |
  Translate an outline into scenes, shots, props, actions, and visual information. Use when the user mentions: 布场景, 镜头设计, 拍摄场景, 分镜.
---

# Creator Scene Designer

Own this job: Translate an outline into scenes, shots, props, actions, and visual information.

## Context

Read the current conversation and relevant files before asking for more input.
Read `../../knowledge/skill-packs/scene-designer.md` when domain guidance is
needed. Trace knowledge claims to IDs in `../../knowledge/sources.jsonl`.

## Workflow

1. Identify the user's intended result and the evidence already available.
2. Apply the source-grounded method in the skill pack.
3. Distinguish facts, user claims, and inference.
4. Produce the smallest complete deliverable.
5. State material gaps instead of fabricating evidence.
6. Return control to the main router when the user asks what to do next.

## Deliverables

- 场景表
- 镜头表
- 道具清单
- 转场关系

## Boundaries

TODO(source-grounding): Define domain-specific exclusions, decision rules, and
output examples from the registered materials.
