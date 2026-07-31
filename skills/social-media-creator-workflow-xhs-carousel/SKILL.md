---
name: social-media-creator-workflow-xhs-carousel
description: |
  Turn approved content into a consistent multi-page Xiaohongshu carousel using exact-text HTML or generated imagery. Use when the user mentions: 小红书组图, 多页图文, 3:4知识卡片, 可截图HTML.
---

# Xiaohongshu Carousel Creator

把已确认内容拆成一组可发布的小红书多页图文。需要文字完全准确、可修改时使用
自包含 HTML；视觉表达优先且允许人工复核文字时，使用图片生成能力。

## Context

先读取完整成稿、目标受众、封面文案和用户视觉要求，再完整读取
`../../knowledge/skill-packs/xhs-carousel.md`。内容尚未完成时退回 `content-writer`；
只需要一张首图时用 `xhs-cover`。

## Workflow

1. 提取核心承诺、最小完整链路、可带走的模板/步骤/清单和必须保留的事实。
2. 先给每页定义唯一任务：首图负责进入，第二页建立继续阅读理由，中间页兑现，末页总结或行动。
3. 根据文字准确性和视觉需求选择 HTML 或图片生成模式；用户已指定时直接执行。
4. 全组使用同一组色彩、字体层级、留白和装饰规则，页面布局可随信息变化。
5. HTML 模式生成一个离线可打开的自包含文件，每页固定 3:4，不依赖外链资源。
6. 图片模式逐页生成或编辑，严格使用已确认文字；发现中文错误时局部修正，仍不稳定则切换 HTML。
7. 检查页数、顺序、文字、溢出、手机可读性、重复信息和跨页一致性后交付。

## Deliverables

- 页级大纲
- 一个多页 HTML 或一组图片
- 视觉规则
- 质量检查结果

## Boundaries

- 不把一张封面需求扩成组图。
- 不复制第三方样式库、品牌视觉、模板或素材。
- 不为了凑页数重复同一观点。
- 涉及医疗、法律、金融收益时不制作确定性承诺。
- HTML 或图片没有实际生成时，不用文字方案冒充成品。
