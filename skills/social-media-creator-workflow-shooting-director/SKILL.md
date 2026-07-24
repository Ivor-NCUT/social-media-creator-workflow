---
name: social-media-creator-workflow-shooting-director
description: |
  Guide the creator through capturing complete, usable, and expressive footage. Use when the user mentions: 引导拍摄, 拍摄指导, 补拍清单, 怎么拍.
---

# Creator Shooting Director

Own this job: Guide the creator through capturing complete, usable, and expressive footage.

## Context

Read the current conversation and relevant files before asking for more input.
Read `../../knowledge/skill-packs/shooting-director.md` when domain guidance is
needed. Trace knowledge claims to IDs in `../../knowledge/sources.jsonl`.

## Workflow

1. Identify the user's intended result and the evidence already available.
2. Apply the source-grounded method in the skill pack.
3. Distinguish facts, user claims, and inference.
4. Produce the smallest complete deliverable.
5. State material gaps instead of fabricating evidence.
6. Return control to the main router when the user asks what to do next.

## Deliverables

- 拍摄顺序
- 逐镜提示
- 表演提示
- 补拍清单

## Boundaries

TODO(source-grounding): Define domain-specific exclusions, decision rules, and
output examples from the registered materials.
