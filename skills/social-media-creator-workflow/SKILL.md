---
name: social-media-creator-workflow
description: |
  A creator-first MOE skill system for moving social media content from topic selection to reusable content assets.
---

# Social Media Creator Workflow

这是创作者工作流的唯一主入口。先阅读当前对话、用户提供的素材和已有结果，
再选择一个最匹配当前工序的专家。除非用户明确要求跑完整流程，否则一次只处理
一个工序。

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
| Xiaohongshu Cover Creator | `social-media-creator-workflow-xhs-cover` | Generate, edit, or learn a Xiaohongshu cover style with Codex image generation and 18 presets adapted from Vivi's xhs-cover-skill. | 小红书封面、xhs封面、生成封面、修改封面 |
| Creator Data Organizer | `social-media-creator-workflow-data-organizer` | Normalize creator-provided screenshots or CSV exports into a comparable, auditable content dataset. | 数据整理、后台截图、CSV分析、运营数据清洗 |
| Creator Strategy Reviewer | `social-media-creator-workflow-strategy-reviewer` | Turn normalized performance data into evidence-based content strategy and testable next actions. | 策略复盘、运营建议、数据复盘、下一步怎么做 |
| Creator Asset Distiller | `social-media-creator-workflow-asset-distiller` | Convert completed work and validated lessons into reusable creator assets with provenance and usage limits. | 内容资产沉淀、方法复用、素材库、经验沉淀 |

## Routing workflow

1. 先读取 `knowledge/project-profile.md`，复用对话中已有的账号定位、受众、
   IP、平台、商业目标和内容资产；不要让用户重复提供。
2. 判断用户要的是“产生新内容”“加工已有内容”“评价现有内容”还是“从结果
   中学习”，再选择一个专家。
3. 如果输入足以完成当前工序，直接执行；如果两条路会产生明显不同结果，最多
   问一个决定性问题。
4. 专家交付后，只说明最自然的下一步，不自动把整条流程跑完。
5. 用户明确指定工序时，以用户意图覆盖默认路由。

## Adjacent-stage tie breakers

- 用户还在决定“讲什么”时用 `topic-selector`；选题已经确定、要组织结构时用
  `outline-builder`。
- 用户要的是内容逻辑和段落时用 `outline-builder`；要的是地点、镜头、动作和
  道具时用 `scene-designer`。
- 用户在拍摄前需要镜头方案时用 `scene-designer`；已经准备开拍或需要补拍时用
  `shooting-director`。
- 用户需要文字成稿时用 `content-writer`；需要从原始素材中决定保留和删除时用
  `rough-cut-planner`。
- 故事顺序尚未稳定时用 `rough-cut-planner`；结构已稳定、要做字幕、音乐和包装
  时用 `fine-cut-planner`。
- 用户要修改方案时进入对应生产工序；用户要判断是否能发布以及应退回哪里时用
  `content-reviewer`。
- 用户要发布包装时用 `multiplatform-distributor`；用户提供发布后的截图或 CSV
  时用 `data-organizer`。
- 用户要标题、正文、标签等整套发布包装时用 `multiplatform-distributor`；用户
  要直接生成、修改或学习小红书封面风格时用 `xhs-cover`。
- 用户要清洗和统一数据时用 `data-organizer`；用户要基于数据做决策时用
  `strategy-reviewer`。
- 用户要下一轮运营动作时用 `strategy-reviewer`；用户要把经验写入可复用模板和
  素材库时用 `asset-distiller`。

## Workflow feedback loops

- 审片不通过时，按问题回退到 `content-writer`、`shooting-director`、
  `rough-cut-planner` 或 `fine-cut-planner`。
- 策略复盘的结论优先回流到 `topic-selector`，必要时再影响提纲与分发。
- 资产沉淀的结果进入项目档案和知识资产，供下一轮选题、提纲和拍摄复用。

## Boundaries

- Do not perform every specialist job inside this router.
- Do not prescribe a fixed expert chain in advance.
- Do not invent source-backed claims when the knowledge assets are incomplete.
- Read `knowledge/sources.jsonl` before using imported domain material.
- 不替用户判断其是否“有资格”做企业主 IP。
- AI 可以按用户要求完成头脑风暴、初稿、终稿或完整交付，不人为限制使用阶段。
- 平台规则、流量比例、红利期和发布时间属于时效性观点；没有当前证据时标明来源
  日期和不确定性，不把它们写成永久事实。

## Source grounding

两份用户提供的方法论材料只用于原创蒸馏。来源授权未确认前：

- 不复制长段原文、独特品牌表达或无法核验的绝对结论；
- 可使用已抽象的方法、判断维度和工作流程；
- 所有知识原子和案例必须带 `source_ids`；
- 对材料之间已经裁决的冲突，以本项目规则为准：开头同时提供多种流派；数据问题
  进入数据整理与策略复盘；不做企业主 IP 资格判断；AI 按用户指令参与任意阶段。
