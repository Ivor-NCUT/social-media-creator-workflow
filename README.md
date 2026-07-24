<div align="center">

# 🎬 Social Media Creator Workflow

### 从一个选题，到一套会持续变聪明的内容生产系统

![Version](https://img.shields.io/badge/version-1.0.0-16a34a?style=for-the-badge)
![Workflow](https://img.shields.io/badge/workflow-12_steps-0f766e?style=for-the-badge)
![Skills](https://img.shields.io/badge/MOE-1_router_%2B_12_experts-2563eb?style=for-the-badge)
![License](https://img.shields.io/badge/license-Proprietary-334155?style=for-the-badge)

一个以创作者真实工作流为骨架的多专家 Agent Skill 项目。
用户只需记住一个入口，也可以从任意创作工序直接开始。

</div>

---

## ✨ 它能做什么

这套 Skills 覆盖内容生产、发布、复盘和沉淀的完整闭环：

```mermaid
flowchart LR
    A[定选题] --> B[出提纲]
    B --> C[布场景]
    C --> D[引导拍摄]
    D --> E[出文章]
    E --> F[粗剪]
    F --> G[精剪]
    G --> H[审片]
    H --> I[多平台分发]
    I --> J[数据整理]
    J --> K[策略复盘]
    K --> L[内容资产沉淀]
    L -. 复用资产 .-> A
    H -. 退回修改 .-> E
    K -. 策略回流 .-> A
```

每个工序由一个独立专家负责。主路由只判断当前最适合进入哪一步，不会把所有方法
堆进一个巨型提示词，也不会强迫用户从头跑完整条链路。

## 🚀 快速开始

### 安装

该仓库目前为私有仓库，请先确认 `gh` 已登录有权限的 GitHub 账号：

```bash
cd ~/.codex/skills
gh repo clone Ivor-NCUT/social-media-creator-workflow
```

重启 Codex 或开启新会话后即可使用。

### 只记一个入口

直接说：

```text
使用 social-media-creator-workflow。
我已经有一条关于 AI 求职的选题，帮我出提纲，并给我 5 种不同机制的开头。
```

主路由会把任务交给 `outline-builder`。已有上下文会继续复用，无需重新填写整套
账号资料。

### 直接调用某个工序

```text
使用 social-media-creator-workflow-data-organizer。
这是过去 30 条小红书内容的后台 CSV，请统一字段、计算能计算的比率，
并标出缺失项和不可比数据。
```

## 🧩 1 个主路由 + 12 个专家

| 工序 | Skill | 主要交付 |
|---|---|---|
| 🧭 总控 | `social-media-creator-workflow` | 当前工序识别、动态路由、回退与回流 |
| 01 定选题 | `social-media-creator-workflow-topic-selector` | 选题候选、评分、内容使命、系列归属 |
| 02 出提纲 | `social-media-creator-workflow-outline-builder` | 多版本开头、标题方向、结构提纲 |
| 03 布场景 | `social-media-creator-workflow-scene-designer` | 场景表、镜头表、道具与转场 |
| 04 引导拍摄 | `social-media-creator-workflow-shooting-director` | 拍摄顺序、逐镜提示、补拍清单 |
| 05 出文章 | `social-media-creator-workflow-content-writer` | 口播稿、旁白、图文、文章或字幕稿 |
| 06 粗剪 | `social-media-creator-workflow-rough-cut-planner` | 素材取舍、粗剪时间线、补拍点 |
| 07 精剪 | `social-media-creator-workflow-fine-cut-planner` | 节奏、字幕、BGM、包装与导出标注 |
| 08 审片 | `social-media-creator-workflow-content-reviewer` | 审核结论、问题优先级、回退工序 |
| 09 多平台分发 | `social-media-creator-workflow-multiplatform-distributor` | 平台标题、封面、正文与关键词 |
| 10 数据整理 | `social-media-creator-workflow-data-organizer` | 标准化数据、派生指标、异常记录 |
| 11 策略复盘 | `social-media-creator-workflow-strategy-reviewer` | 诊断、置信度、实验与行动计划 |
| 12 资产沉淀 | `social-media-creator-workflow-asset-distiller` | 复用模板、证据、来源与使用边界 |

## 🧠 内嵌的方法论

- 从目标用户的观看动机出发，再匹配创作者真实资源。
- 一条内容先确定主要使命：流量、涨粉、转化、调性或表达。
- 同一主题同时提供直接价值、好奇、反常识、矛盾等开头版本。
- 标题和开头承诺的价值必须在正文中兑现。
- VLOG 检查真实、反差、交互和叙事主线。
- 粗剪先解决故事与信息，精剪再处理字幕、音乐和包装。
- 单条数据不足以否定账号方向，策略结论必须带证据与置信度。
- 单次偶然高数据先记录为待验证假设，不直接固化成成功公式。

## 📊 CSV 数据整理

数据整理专家附带纯 Python 标准库脚本：

```bash
python3 \
  skills/social-media-creator-workflow-data-organizer/scripts/normalize_creator_csv.py \
  source.csv normalized.csv
```

脚本会：

- 映射常见中英文后台字段；
- 保留无法识别的原始字段；
- 仅在分母有效时计算派生比率；
- 拒绝多个原字段静默覆盖同一个标准字段。

## 🏗️ 项目结构

```text
social-media-creator-workflow/
├── skills/                 # 主路由与 12 个专家
├── knowledge/
│   ├── skill-packs/        # 每个专家专用方法
│   ├── atoms/              # 可追溯方法原子
│   ├── cases/              # 场景、决策与经验
│   ├── project-profile.md  # 创作者项目档案
│   └── workflow-contract.md
├── docs/architecture.md
├── tests/
└── tools/validate_project.py
```

详细边界与数据流见 [`docs/architecture.md`](docs/architecture.md)。

## ✅ 验证

```bash
python3 tools/validate_project.py .
python3 -m unittest discover -s tests -v
python3 -m unittest discover \
  -s skills/social-media-creator-workflow-data-organizer/tests -v
```

本地有 `uv` 时，可进一步验证所有 Skill frontmatter：

```bash
for skill in skills/*; do
  uv run --with pyyaml python \
    /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$skill"
done
```

## 🔐 来源与分发边界

本项目的方法来自用户提供的两份材料，经原创抽象后写入 Skills。原始材料的公开
再分发授权尚未确认，因此：

- 仓库暂时保持私有；
- 不复制长段原文或独特品牌表达；
- 平台规则、流量比例和红利期等时效性观点不作为永久事实；
- 公开发布前需要重新确认材料权利和许可证。

## 🗺️ 参与开发

开发采用“一条 Issue 对应一个可验收工序”的方式。每项完成后先运行最小测试，
再单独提交和关闭 Issue。新增专家时请同步更新：

1. `project.json`
2. 主路由 Expert map
3. `knowledge/skill-packs/`
4. `docs/architecture.md`
5. 对应 `evals/evals.json`

---

<div align="center">

**让每一次创作，都能给下一次留下可复用的东西。**

</div>
