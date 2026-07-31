---
name: social-media-creator-workflow-positioning
description: |
  Turn creator assets, audience, goals, and sustainable supply into an account positioning and initial content system. Use when the user mentions: 账号定位, 起号定位, 人设定位, 内容支柱.
---

# Creator Positioning

把创作者真实拥有的资源、想服务的人、经营目标和可持续供给，整理成可验证的账号定位。
定位完成后停止，不替 `topic-selector` 批量展开具体选题。

## Context

先读取当前对话、已有账号资料和 `../../knowledge/project-profile.md`，再完整读取
`../../knowledge/skill-packs/positioning.md`。需要当前赛道证据时调用
`reach-research`，不得把未经验证的平台印象当市场事实。

## Workflow

1. 盘点创作者的身份、经验、能力、素材、表达方式、商业目标和持续投入边界。
2. 明确主要受众、反复出现的具体问题，以及账号希望建立的关系。
3. 生成少量候选定位，用资源匹配、用户价值、差异证据、持续供给和目标一致性比较。
4. 输出一句可检验的定位、账号识别要素和 3～5 个内容支柱。
5. 设计最小验证周期：先发布一组覆盖不同支柱的内容，再根据真实数据调整。
6. 把已确认定位写成可交给 `topic-selector` 的约束，不把“前若干篇”伪装成长期定论。

## Deliverables

- 定位候选与取舍
- 定位句
- 账号识别要素
- 内容支柱与验证计划

## Boundaries

- 不承诺起号速度、粉丝量或必然变现。
- 不因赛道热门就忽略创作者资源和持续供给。
- 不虚构人设、履历、案例或专业资质。
- 已有账号表现异常但定位未必错误时，先交 `account-audit` 诊断，不直接推倒重来。
