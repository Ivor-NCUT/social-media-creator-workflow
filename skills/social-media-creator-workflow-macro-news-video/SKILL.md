---
name: social-media-creator-workflow-macro-news-video
description: |
  Turn one current macroeconomic, policy, labor, technology, industry, or social-trend news item into a sourced Chinese vertical explainer video, including the angle, narration, cover copy, storyboard, HyperFrames project, captions, cover image, and rendered MP4. Use when the user asks for 全自动宏观热点解读视频, 宏观新闻视频, 新闻解读成片, HyperFrames 新闻视频, or 输入新闻自动生成视频.
---

# 全自动宏观热点解读视频

输入一条新闻，交付一套可追溯的观点与实际成片。默认直接跑完整流程；只有事实不足、
来源互相冲突、缺少运行时或内容可能造成重大误导时才停下。

## 先读

1. 完整读取 `../../knowledge/skill-packs/macro-news-video.md`。
2. 需要理解参考账号时读取 `references/macro-prism-study.md`；不得复制其名称、Logo、
   逐句文案、截图或独特品牌表达。
3. 开始生成工程前读取 `references/hyperframes-pipeline.md`，并调用已安装的
   `hyperframes` 与 `hyperframes-cli` Skill。HyperFrames 是外部依赖，不复制其实现。

## 输入与事实门

- 接受新闻正文、链接或“正文 + 链接”；平台默认竖屏短视频，语言默认中文。
- 先固定 `as_of` 日期。公开事实优先原始公告、政策原文、统计机构、公司披露和论文，
  再用至少一条独立来源交叉核对关键数字。
- 每个会进入旁白的可核验主张都写入 `source-ledger.json`。找不到来源的数字、因果和
  “全国第一”等比较词不得进入成片；争议信息必须在旁白中明确标注不确定性。
- 新闻已过时、事实本身不成立或没有可解释的机制时，返回证据缺口，不硬做视频。

## 生产流程

1. **定切角**：从表层事件向下追一层，寻找资源重配、成本转移、激励变化、供需错位或
   旧规则失效。用一句“大家在看 X，我更关心 Y”写入 `angle-brief.md`。
2. **写脚本**：采用“新闻钉子 → 尺度翻译 → 反常识问题 → 机制拆解 → 利益相关者 →
   判断回扣”。默认使用 ListenHub Voice 一次生成 85–110 秒的连贯旁白、约 450–650 个
   中文字符；每 20–35 秒给一个数字、对比、
   改名或问题作为认知台阶。
3. **做封面**：`cover-brief.json` 提供 3 个候选，只选 1 个生成。主标题 6–24 个非空白
   字符，写“结论或冲突”，不写“某新闻解读”；副标题补代价、机制或疑问。
4. **做分镜**：`storyboard.json` 中每个场景只承担一个判断，绑定旁白和证据 ID；数字用
   对比、刻度、流向或前后变化呈现，不把长段旁白重新贴满屏幕。
5. **生成声音并建工程**：先调用已安装的 `listenhub-voice` Skill，用
   `ListenHub-Voice-1.0` 将完整脚本一次生成连贯中文旁白；再写 `video/DESIGN.md`，用
   HyperFrames 创建 1080×1920 工程并转写词级字幕、制作场景转场与封面英雄帧。所有
   时间线必须确定性、可 seek。
6. **验收并渲染**：依次运行 `hyperframes lint`、`hyperframes check`，需要定位布局时再
   `inspect --json`；修完错误和非故意溢出后再 `render`。从已渲染视频的封面英雄时刻
   提取 `cover.png`。
7. **检查交付**：运行 `python3 scripts/validate_story_package.py <job-dir> --stage final`，
   返回 MP4、封面、完整稿、来源台账、工程路径和实际验证结果。

## 完成标准

- `source-ledger.json`、`angle-brief.md`、`script.md`、`cover-brief.json`、
  `storyboard.json`、`video/DESIGN.md`、`video/index.html`、`video/listenhub-task.json`、
  `video/final.mp4` 与 `video/cover.png` 全部存在。
- 片头前 8 秒同时交代新闻钉子、尺度或冲突；结尾回扣开头并给出判断，不用空泛
  “关注我”。
- 旁白讲因果，画面讲结构，字幕只承担阅读辅助；三者不逐字重复。`narration.wav` 必须
  来自一次 ListenHub Voice 成功任务并保留任务 ID、时长和来源 URL 的非敏感记录。
- 关键数字可由证据 ID 回查；推断与事实分开。
- HyperFrames 的 lint、check 全部通过；成片能够播放，封面文字无乱码。

## 边界

- 不把“有争议”当流量捷径，不制造政策恐慌、投资建议或单因果结论。
- 不因“全自动”跳过事实核验、版权边界、对真人的伤害检查或最终成片回看。
- 不自动发布到平台；发布是独立授权动作。
- ListenHub Voice 文本最多 1400 字、`durationHint` 最多 110 秒。证据链超过单条容量时
  拆成系列视频，不把多段音频拼接后冒充一次端到端生成。
- ListenHub 未登录、缺少 OpenAPI Key、余额不足或任务失败时保留文字和工程，明确报告
  阻塞；不回退本地 TTS，也不用英文声音冒充中文。
