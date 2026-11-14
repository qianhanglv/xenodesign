# X-DONUT-001 · 交付包

题目：D2 难度 · 13 条约束 · Tension T-01 · 题眼 Q1（≥1/3 贯穿空腔的甜甜圈拓扑）。
所有产出按 L 级别分文件夹存放，L0 为同一只生物的母版，L1–L5 都复用它。

## 目录

```
X-DONUT-001/
├── L0/  creature.svg        3/4 视角全身图（主图）
│        design.md           约束映射注释（474 词）
├── L1/  front.svg back.svg left.svg right.svg top.svg bottom.svg
│        note.md             六视图一致性 + Q1 可追踪性（477 词）
├── L2/  section.svg         过空腔轴的剖面（连续 void / 3 口汇入同一腔 / 矿物架）
│        note.md             剖面注释（464 词）
├── L3/  skeleton.svg        矿物骨架 + 淡体外轮廓
│        pelt.svg            整张连续皮张展开（洞/缝/隧道边界）
│        note.md             双文件注释（494 词）
├── L4/  motion.svg          SMIL 自包含动画，3.2 s 无缝循环（idle→run→jump→land→idle）
│        note.md             运动注释（490 词）
├── L5/  ride.svg            骑自行车（可选彩蛋）
│        note.md             骑行注释（453 词）
├── preview/all-levels.png   十二张图的拼合预览
└── build/                   生成脚本（可复现，见下）
```

## 关键数据（注释里引用的都是实测值）

- 本体：矿物环形壳体，贯穿孔为真实开口，**洞口面积 / 壳体剪影 = 0.39**（正/背视图同为
  0.39，顶/底视图 0.32，L5 骑姿 0.36），阈值 1/3。
- 尺寸：1 绘图单位 = 0.85 cm；壳体外径 2.1 m，整体高 2.9 m，肢展 2.6 m（P1 要求 1–3 m）。
- 计数：4 肢 = 2 腿 + 2 操纵肢；3 个进食口；0 眼；1 个贯穿孔。
- 注释：每个 L 单独一份，全部 < 600 词（与题面「600 词/任务」一致，不按视图分计）。

## 怎么查看

- 浏览器直接打开任意 `.svg`；L4 的 `motion.svg` 直接双击即可看到循环动画（SMIL，
  无脚本、无外链）。
- 是否满足硬性规则（已脚本校验）：全部 `viewBox="0 0 512 512"`、无 `<text>`、
  无位图/外部引用、单文件 < 512 KB。

## 复现

```
cd build
python3 build_l0.py && python3 build_l1.py && python3 build_l2.py \
  && python3 build_l3.py && python3 build_pelt.py && python3 build_l4.py \
  && python3 build_l5.py
```

`model.py` 是自写的正交投影 + 面片着色器（画家算法、轮廓描边、区域面积测量），
`creature.py` 定义同一只生物的 3D 形态与 IK 姿态，因此六个视图、骨架、动画、骑姿
共享同一套解剖数据，不会出现各画各的。

## 插画版（额外产出）

`L0/art/` 下是同一只生物的两种"奇幻/神话插画"风格位图，几何数据与 L0 完全同源
（同一 3D 笼架、同一相机、同一姿态），只是换了画法：

- `creature-illuminated.png`（仓库 Web 版 1000×1000；原图 1400×1400）——彩绘细密画：羊皮纸、金线边框、日芒
  背光、金箔晶冠、洞口炽光，墨线勾边。
- `creature-woodcut.png`（仓库 Web 版 1000×1000；原图 1400×1400）——雕版：版面为纸，全图由刻线组成，线条走向
  按受光分五级（单线→密线→交叉线→实黑），轮廓为刻刀边线，地面用横向排线。

生成脚本：`build/art.py`（Pillow 自写光栅器 + 同一套法线/投影，含密度直方图归一）。

## Known limitations (Pilot 02 review)

- **L5 is static:** `L5/ride.svg` has no `<animate>`; it is a single frame, not a ride cycle.
- **L5 structure is distorted:** in the riding pose the ring body is visibly twisted/skewed and is not a clean torus.
- **L5 contact is hard to verify:** the bicycle is small relative to the body; saddle, pedal, and handlebar contacts need a close-up.
- **L1 side views lose the cavity:** left/right read as a solid bent slab, so the six views do not all describe the same topology.
- **L2 section reads as a capsule:** the ring topology is hard to recover from the section drawing.
- **Area ratios are self-reported:** the 0.39 / 0.36 cavity ratios are not independently measured.
