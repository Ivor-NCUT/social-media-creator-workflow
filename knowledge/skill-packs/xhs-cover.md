# Xiaohongshu Cover Creator knowledge pack

依据 [`Vivixiao980/xhs-cover-skill`](https://github.com/Vivixiao980/xhs-cover-skill)
在 commit `25a7279ff36931fc4eab069999adb1ad988b5d27` 的 Codex 原生流程改编。
作者为 Vivi（[@Vivixiao980](https://github.com/Vivixiao980)）。

## 稳定原则

- 新生成、局部修改、参考图风格学习是三个不同入口。
- 局部修改必须使用上一版或指定封面作为输入，不能从零重做。
- 人物身份、五官、发型和服装主体默认保持一致。
- 只使用用户给出的主标题与副标题，不添加随机文字。
- 主标题优先服务手机信息流可读性，默认比例为 3:4。

## 风格选择

预设风格是生成方向，不是必须逐字复制的提示词。根据内容气质选择一个最接近的
预设；用户有参考图或明确审美要求时，以用户输入为准。

完整预设表位于专家目录的 `references/styles.md`。

## 与相邻专家的边界

- `multiplatform-distributor` 负责封面文案、标题版本和平台发布包。
- `xhs-cover` 负责把已确认文案与视觉素材变成图片，或对现有封面做局部编辑。
- 如果用户同时需要整套发布包和实际封面，先由分发专家确认文案，再进入本专家生成。

## 上游边界

本项目封装 Codex 原生图片生成/编辑路径及 18 种风格词汇，不复制上游 Node.js、
Gemini API 配置、安装脚本和预览大图。命令行备用能力继续由上游项目维护。
