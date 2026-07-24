---
name: social-media-creator-workflow-rough-cut-planner
description: |
  Build the first coherent edit from raw footage while preserving the story and identifying missing material. Use when the user mentions: 粗剪, 素材筛选, 粗剪时间线, 整理素材.
---

# Creator Rough Cut Planner

Own this job: Build the first coherent edit from raw footage while preserving the story and identifying missing material.

## Context

Read the current conversation and relevant files before asking for more input.
Read `../../knowledge/skill-packs/rough-cut-planner.md` when domain guidance is
needed. Trace knowledge claims to IDs in `../../knowledge/sources.jsonl`.

## Workflow

1. Identify the user's intended result and the evidence already available.
2. Apply the source-grounded method in the skill pack.
3. Distinguish facts, user claims, and inference.
4. Produce the smallest complete deliverable.
5. State material gaps instead of fabricating evidence.
6. Return control to the main router when the user asks what to do next.

## Deliverables

- 粗剪时间线
- 保留片段
- 删除片段
- 补拍点

## Boundaries

TODO(source-grounding): Define domain-specific exclusions, decision rules, and
output examples from the registered materials.
