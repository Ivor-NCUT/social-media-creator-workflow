---
name: social-media-creator-workflow-asset-distiller
description: |
  Convert completed work and validated lessons into reusable creator assets with provenance and usage limits. Use when the user mentions: 内容资产沉淀, 方法复用, 素材库, 经验沉淀.
---

# Creator Asset Distiller

把已完成内容、用户反馈和策略复盘结论转成可复用的创作资产。每项资产记录来源、
证据、适用范围和限制，区分已验证资产与待验证假设。

## Context

先读取本轮内容版本、发布包、数据整理、策略复盘和项目档案，再完整读取
`../../knowledge/skill-packs/asset-distiller.md`。

## Workflow

1. 盘点本轮可沉淀的选题、开头标题、用户问题、IP故事、场景镜头、写作结构、
   剪辑模式、关键词和失败教训。
2. 为每项资产确定最小可复用单元，不保存无上下文的大段成稿。
3. 记录直接来源、适用平台、人群、内容使命和使用限制。
4. 根据证据标记 `validated`、`hypothesis` 或 `deprecated`。
5. 合并重复资产；内容相似但边界不同的保留差异。
6. 输出 Markdown 索引和 JSONL 记录，说明它会回流到哪些工序。

## Deliverables

- 内容资产
- 复用模板
- 来源记录
- 使用边界

JSONL 字段：`id`、`type`、`title`、`content`、`status`、`source_refs`、
`platforms`、`audiences`、`missions`、`evidence`、`limits`、`feeds_stages`。

## Boundaries

- 单次高数据默认是 `hypothesis`，除非有重复证据或用户明确验证。
- 不保存密钥、私人身份信息或未授权素材。
- 不把时效性平台观点升级为长期资产。
- 不为了沉淀而复制整篇来源材料或完整成稿。
- 不覆盖用户已经确认的项目档案，冲突时保留新记录并标记待裁决。
