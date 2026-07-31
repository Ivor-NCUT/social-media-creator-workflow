---
name: social-media-creator-workflow-xhs-cover
description: |
  Generate, edit, or learn a Xiaohongshu cover style with Codex image generation and 18 presets adapted from Vivi's xhs-cover-skill. Use when the user mentions: 小红书封面, xhs封面, 生成封面, 修改封面.
---

# Xiaohongshu Cover Creator

把已经确认的内容包装直接做成小红书封面。优先使用 Codex 原生图片生成或编辑能力，
不要求用户额外配置 API。

本专家改编自 Vivi（[@Vivixiao980](https://github.com/Vivixiao980)）的
[`xhs-cover-skill`](https://github.com/Vivixiao980/xhs-cover-skill)。使用前完整读取
`../../knowledge/skill-packs/xhs-cover.md` 和 `references/styles.md`。

## Intent

- **生成**：用户提供人物图或主视觉、标题和风格后，生成新封面。
- **修改**：用户要求基于上一版调整时，必须编辑指定封面，只改点名内容。
- **学习风格**：用户提供参考图时，提取配色、字体气质、构图、装饰和留白，再用
  提取结果生成封面。

## Workflow

1. 复用 `multiplatform-distributor` 已确认的封面文案；缺少时只收集人物图/主视觉和
   主标题，副标题、风格、比例与生成张数有明确要求才追加。
2. 比例默认 3:4。未指定风格时，根据内容气质从 `references/styles.md` 选一个并
   简短说明，不让用户重复浏览 18 项。
3. 新生成时，把人物图、标题、风格说明、比例和用户限制一起交给图片生成能力。
4. 修改时，把上一版或用户指定封面作为编辑输入，保留人物身份、构图、色彩和未点名
   元素，只改明确要求。
5. 学习风格时，先从 1–5 张参考图提取稳定视觉特征，再生成；不复制原图中的品牌
   标识、人物身份或受保护角色。
6. 需要多版本测试时，每版只改变一个可描述的构图或信息层级变量，保持标题、主体和
   其他条件一致；不把随机重绘冒充 A/B 测试。
7. 返回生成图片、采用的风格、比例和本次修改摘要。

## Prompt contract

生成提示词必须包含：

```text
生成一张小红书 {比例} 封面。
保持输入人物的身份、五官、发型和服装主体自然一致。
风格：{预设风格或提取出的视觉特征}
主标题：{主标题}
副标题：{可选}
要求：主标题最大且适合手机信息流阅读；严格使用给定文字，不添加随机中英文；
中文准确、无乱码；不要添加水印、平台标识或未要求的品牌元素。
```

修改提示词必须明确“基于输入封面局部编辑，不重新设计整张图”，并列出唯一允许改变
的内容。

## Deliverables

- 封面图片
- 风格选择
- 比例与版式说明
- 修改记录（仅修改任务）

## Boundaries

- 不用文字描述冒充已经生成的图片。
- 不在缺少目标图片时声称完成了局部编辑。
- 不将平台规则、尺寸或流量偏好写成永久事实；默认 3:4 只是当前工作流默认值。
- 不内置上游 Node.js / Gemini CLI 备用路径；需要命令行生成时，使用并遵循上游
  [`xhs-cover-skill`](https://github.com/Vivixiao980/xhs-cover-skill)。
- 上游来源、作者和许可证见仓库 `THIRD_PARTY_NOTICES.md`。
