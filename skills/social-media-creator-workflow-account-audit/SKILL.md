---
name: social-media-creator-workflow-account-audit
description: |
  Diagnose an existing social account or profile and rewrite its public-facing bio from user-provided evidence. Use when the user mentions: 账号体检, 主页诊断, 简介改写, 置顶诊断, 竞品账号分析, 账号不涨粉.
---

# Creator Account Audit

诊断已有账号卡在哪一层，并给出少量优先动作。账号体检处理主页和多篇内容形成的
账号级问题；单篇或一批内容的漏斗复盘交给 `strategy-reviewer`。

## Context

先读取用户提供的主页截图、内容墙、后台数据、目标和对标账号，再完整读取
`../../knowledge/skill-packs/account-audit.md`。公开账号研究需要当前证据时调用
`reach-research`；数据字段未归一时先交 `data-organizer`。

## Workflow

1. 记录诊断对象、账号目标、证据来源、时间窗口和数据缺口。
2. 分别检查定位可理解性、内容一致性、包装识别、发布连续性、互动结构和关注转化。
3. 所有判断引用可见元素或数据；估算值必须标明估算和计算方式。
4. 先定位最可能的瓶颈，再列支持、反对和缺失证据，不平均优化所有维度。
5. 对标时区分可迁移方法与不可迁移的身份、资源、历史流量和预算。
6. 给 3～5 个按影响排序的改动，并把每项路由到定位、选题、分发、封面或策略复盘。
7. 用户只要主页简介时，检查“你是谁、帮谁、解决什么、凭什么可信、下一步做什么”，
   然后给少量不同侧重的简介版本，不输出整套账号审计。

## Deliverables

- 证据边界
- 账号诊断
- 瓶颈与置信度
- 优先改动与接力工序
- 需要时的简介与置顶改写

## Boundaries

- 不抓取私密数据，不绕过平台限制，不刷互动或批量养号。
- 不把无来源行业均值当评分基准。
- 不把相关性写成因果关系。
- 证据不足时输出可完成的定性诊断与补数清单，不编造分数。
