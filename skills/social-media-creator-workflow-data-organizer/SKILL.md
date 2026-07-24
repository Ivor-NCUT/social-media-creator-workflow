---
name: social-media-creator-workflow-data-organizer
description: |
  Normalize creator-provided screenshots or CSV exports into a comparable, auditable content dataset. Use when the user mentions: 数据整理, 后台截图, CSV分析, 运营数据清洗.
---

# Creator Data Organizer

把用户提供的平台后台截图或 CSV 整理成可比较、可审计的数据集。这里只建立事实
底座，不提前给运营策略。

## Context

先读取平台、账号、统计周期、截图/文件和字段说明，再完整读取
`../../knowledge/skill-packs/data-organizer.md`。CSV 可使用
`scripts/normalize_creator_csv.py` 做确定性归一化。

## Workflow

1. 记录数据来源、平台、账号、导出/截图时间和统计窗口。
2. 建立原字段到标准字段的映射，保留未识别字段。
3. 截图只提取清晰可见的数字；模糊值标为缺失并注明位置。
4. 检查单位、百分比、累计/区间口径和不同平台定义。
5. 只有字段充分时才计算点击率、互动率、收藏率和关注转化。
6. 按内容使命、系列、选题、开头类型、平台和版本打标签。
7. 输出异常、缺失、不可比项和可进入策略复盘的数据摘要。

## Deliverables

- 标准化数据
- 派生指标
- 异常记录
- 数据摘要

标准字段与计算口径见方法包。结果必须同时保留来源字段或映射记录，便于复核。

## Boundaries

- 不补猜截图中看不清的数字。
- 不把曝光、播放、观看人数、阅读量等不同字段强行当成同一指标。
- 不在没有分母时计算比率。
- 不根据数据直接判断内容策略；策略建议交给 `strategy-reviewer`。
