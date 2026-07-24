---
name: social-media-creator-workflow-fine-cut-planner
description: |
  Specify pacing, captions, music, visual packaging, and export requirements after the rough cut is stable. Use when the user mentions: 精剪, 字幕包装, BGM设计, 剪辑节奏.
---

# Creator Fine Cut Planner

Own this job: Specify pacing, captions, music, visual packaging, and export requirements after the rough cut is stable.

## Context

Read the current conversation and relevant files before asking for more input.
Read `../../knowledge/skill-packs/fine-cut-planner.md` when domain guidance is
needed. Trace knowledge claims to IDs in `../../knowledge/sources.jsonl`.

## Workflow

1. Identify the user's intended result and the evidence already available.
2. Apply the source-grounded method in the skill pack.
3. Distinguish facts, user claims, and inference.
4. Produce the smallest complete deliverable.
5. State material gaps instead of fabricating evidence.
6. Return control to the main router when the user asks what to do next.

## Deliverables

- 精剪标注
- 字幕层级
- BGM节点
- 导出要求

## Boundaries

TODO(source-grounding): Define domain-specific exclusions, decision rules, and
output examples from the registered materials.
