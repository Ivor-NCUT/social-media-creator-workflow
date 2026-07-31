# Creator Data Organizer knowledge pack

依据 `creator-methods-collection-a` 与项目已确认的数据流程蒸馏。

## 来源元数据

每批数据记录：平台、账号、来源类型、统计开始/结束、导出或截图时间、时区、内容
数量和用户说明。

## 标准字段

- `content_id`、`title`、`publish_time`；
- `impressions`、`views`；
- `likes`、`comments`、`saves`、`shares`、`follows`；
- `search_views`、`completion_rate`；
- `content_mission`、`series`、`topic`、`opening_type`、`platform_version`。

字段不存在时留空。不同平台的“曝光”和“播放”必须保留原定义。

## 派生指标

只有分母存在且大于 0 才计算：

- 点击/播放转化 = views / impressions；
- 互动率 = (likes + comments + saves + shares) / views；
- 收藏率 = saves / views；
- 关注转化 = follows / views；
- 搜索占比 = search_views / views。

输出使用小数值，并说明展示时可格式化为百分比。

## 截图

逐张记录截图名称和可见区域。数字模糊、被遮挡、单位不清或时间窗口缺失时，值留空
并写入异常记录。不要用相邻数字推断。

## CSV

优先用脚本按别名映射常见字段。未知字段以 `source__` 前缀保留；多个原字段映射到
同一标准字段时停止并要求人工裁决，避免静默覆盖。

## 可比性

比较前至少核对平台、统计窗口、内容使命和指标定义。流量型与转化型内容可以并列
展示，但策略复盘时不能只按播放量排序。

多篇数据同时保留样本数、分布、中位数、异常值与时间窗口。分组样本过少时只展示
原始记录，不宣称某种选题或包装稳定胜出；分布明显偏斜时不以平均值代表典型表现。

## 交接

数据摘要只描述事实：最高/最低、缺失、异常和分组概况。不解释“为什么”，不提出
换赛道等策略。

本节的多篇比较纪律受 `spacezephyr-creator-buddy-xhs-skills` 启发，仅保留独立表达的
抽象方法。
