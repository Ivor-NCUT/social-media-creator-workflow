# HyperFrames 生产协议

只记录本专家的编排决策；具体 HTML、动画、字幕、转场与 CLI 语法以安装中的
`hyperframes` 和 `hyperframes-cli` Skill 为准。

## 目录契约

```text
<job>/
├── source-ledger.json
├── angle-brief.md
├── script.md
├── cover-brief.json
├── storyboard.json
└── video/
    ├── DESIGN.md
    ├── index.html
    ├── narration.wav
    ├── transcript.json
    ├── cover.png
    └── final.mp4
```

## 调用顺序

```bash
hyperframes init <video-dir> --non-interactive --example blank
HYPERFRAMES_PYTHON="$HOME/.local/share/hyperframes/python/bin/python" \
  hyperframes tts <script.txt> --voice <z_voice> --output <video-dir>/narration.wav
HYPERFRAMES_PYTHON="$HOME/.local/share/hyperframes/python/bin/python" \
  hyperframes transcribe <video-dir>/narration.wav --model small --language zh --dir <video-dir>
hyperframes lint <video-dir>
hyperframes check <video-dir>
hyperframes inspect <video-dir> --samples 15 --json
hyperframes render <video-dir> --output <video-dir>/final.mp4 --quality high
ffmpeg -ss <cover_hero_second> -i <video-dir>/final.mp4 -frames:v 1 <video-dir>/cover.png -y
```

先用 `hyperframes tts --list` 选择 `z` 开头的普通话声音。非英语语音不得用 `.en`
转写模型。若 CLI 版本的参数与这里不同，以当前 `--help` 为准并把真实命令写入交付记录。
若上述 Python 不存在，用 `uv venv "$HOME/.local/share/hyperframes/python"` 创建一次，随后用
`uv pip install --python "$HOME/.local/share/hyperframes/python/bin/python" openai-whisper kokoro-onnx soundfile`
补齐共享运行时；不要在每个视频工程里重复安装。

## DESIGN.md 最小视觉身份

- 画幅：1080×1920；5:6 信息流裁切区内仍能读到主标题。
- 情绪：冷静、锋利、纪录片式数据新闻；不是金融终端仿制，也不是赛博霓虹。
- 颜色：暖黑背景、暖白正文、单一琥珀强调色；具体十六进制值必须写入 DESIGN.md。
- 字体：中文显示字体 + 数据等宽字体；不用 HyperFrames typography 参考中的禁用默认字体。
- 背景：每个场景有一层与主题相关、已授权或可生成的弱化图像，加暗罩保证对比度。
- 动效：中等能量。相关论点用 push/slide，章节转折用 shutter 或 diagonal split，结尾用
  gentle fade；同片不堆满不同转场。

## 场景骨架

1. `cold-open`：新闻来源、日期、事件和第一组尺度数字。
2. `reframe`：指出多数人关注点与本片真正问题的差异。
3. `mechanism-*`：2–4 个机制，每个机制至少一个可视化证据。
4. `who-wins-loses`：把宏观变量翻译成企业、劳动者、消费者或城市的具体变化。
5. `verdict`：回扣标题，用一句可复述判断结束；需要互动时只问与观众经验直接相关的问题。

每个场景先完成静态 hero frame，再用 `gsap.from()` 加入场。非最终场景不做退出动画，
由转场接管退出。多场景不得跳切。

## 字幕与音画分工

- 旁白：解释因果和限定条件。
- 主画面：呈现比较、方向、结构、角色关系和关键数字。
- 底部字幕：3–6 个汉字或一个自然短语一组；只强调数字、主体和转折词。
- 字幕下沿留出平台 UI 安全区；同一时刻只显示一组，并在结束点硬清除。

## 验收

除 CLI 三项检查外，人工抽看 0–8 秒、每个章节英雄帧、结尾 10 秒和 cover.png：

- 无错字、乱码、溢出、低对比与平台 UI 遮挡；
- 封面结论与片中证据一致；
- 画面不是逐字稿，数据与旁白时间对齐；
- 音乐不盖人声，TTS 没有错误断句或数字读法；成片建议约 -14 LUFS，true peak 不高于
  -1 dBTP。
