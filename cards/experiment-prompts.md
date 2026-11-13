已按新版《提示词撰写指南》和《提示词素材库》重写。关键变化：**L3 的"皮张"必须写成"一整张连续皮平铺展开（拓扑皮张），不是剖面也不是爆炸图"**；**L4 最低要求是 `motion.svg` 或 8–12 帧降级，4 帧只够分镜**；素材全部从库中重新随机抽取，中级含加分项。

---

## 一、D1 难度 · L0–L4 全项目（注释上限 300 词/任务）

```text
You are designing an alien creature for XenoDesign. Do not ask questions; produce the output directly.

=== WHAT TO PRODUCE ===
For each level requested below, produce one SVG drawing of a single alien creature, followed by a --- separator, followed by a design note. Levels: L0, L1, L2, L3, L4.

=== SVG RULES ===
- viewBox="0 0 512 512"
- One creature only per drawing.
- No <text> elements, no external references, no raster images, under 512 KB.
- L0: full body, side or 3/4 view (creature.svg).
- L1: six orthographic views — front, back, left, right, top, bottom (front.svg ... bottom.svg).
- L2: cutaway or cross-section (section.svg).
- L3: skeleton.svg + pelt.svg (see L3 rules below).
- L4: motion.svg, or 8-12 frames frame01.svg ... frame12.svg if animation is impossible (see L4 rules below).

=== CONSTRAINT GROUPS AND PRIORITY ===
Constraints are grouped as P (global parameters), F (free design goals), Q (exact counts or prohibitions of repeatable parts), N (body-plan rules). If constraints seem to conflict, follow P > F > Q > N.

=== THE CONSTRAINTS ===
P1: body length 1-10 cm.
F1: lives under a permanent ice sheet.
F2: stores water in a body sac.
Q1: exactly 2 antennae.
Q2: no more than 4 limbs.
Q3: exactly 1 tail.

=== L1 RULES ===
Using the same creature as the source, draw six orthographic views: front, back, left, right, top, bottom. One SVG per view. Use the same scale and alignment in every view. No perspective. Keep every count, pattern, and proportion identical across views. If a feature is hidden in one view, it still exists in the design; do not delete it. Do not redesign the creature.

=== L2 RULES ===
Using the same creature as the source, draw a cutaway or cross-section (same viewBox). Choose a plane that shows how the body cavity and openings connect. Show the structural material (crystal, mineral, bone, or shell). Do not label the image. Do not redesign the exterior.

=== L3 RULES ===
Using the same creature as the source, draw skeleton.svg: the structural frame with a faint body outline; joints and limbs must align with the exterior; keep the same counts.

Also draw pelt.svg: the skin removed as ONE continuous piece and unfolded flat, like a tiger pelt stretched on the ground. Same viewBox. Show the complete outer surface, the seam/incision lines, and how the pattern continues across them. Treat the skin as a single 2D surface with holes: every opening, eye, limb socket, and tail base must appear as a hole, a boundary, or an extension in the sheet. Show the dorsal / ventral / left / right layout and where the seams run. The sheet must be one connected piece, not several pieces laid side by side. Do NOT draw a cutaway. Do NOT draw an exploded view. Do NOT separate the skin into multiple pieces. Do NOT change the creature's counts or pattern.

=== L4 RULES ===
Using the same creature as the source, animate a full locomotion cycle: idle -> move -> stop -> idle. Output motion.svg: one self-contained animated SVG using SMIL or CSS, same 512x512 viewBox, 2-4 seconds, loop seamlessly. Keep anatomy identical in every frame: same limb count, opening count, pattern, and proportions. Show weight, contact, anticipation, and follow-through. No limb teleportation, no sliding feet, no changing counts. If you cannot animate, output 8-12 frames as frame01.svg ... frame12.svg and say so in the note. A 4-frame storyboard does NOT count as L4.

=== THE DESIGN NOTE ===
- At most 300 words PER TASK (all levels share this cap, not per view).
- One line per constraint, format: P1 -> the visible feature that shows it.
- If a constraint is hidden in this view, say so and where it is.
- L1+: add a line "Source: L0 <id>" declaring the design is reused, not redrawn.
- L3: add a line "PELT: one continuous sheet; seams ...; holes ...".
- L4: add a line "MOTION: loop Xs; contact ...; frames ...".
- If two constraints conflict, add a CONFLICT line.
- Do not write lore.

=== OUTPUT SHAPE ===
For each level:
SVG
---
Design note

=== SELF-CHECK (8 items) ===
1. One creature only per drawing.
2. viewBox is 0 0 512 512.
3. All counts match the constraints in every view.
4. No <text> in the SVG.
5. One note line per constraint.
6. Drawing and note agree; counts and patterns stay consistent across views.
7. Total note is within 300 words for the whole task.
8. L3 pelt is one continuous flat sheet (not a cutaway, not an exploded view); L4 is a real loop or 8-12 frames with a stated fallback; L1+ declares source reuse.
```

---

## 二、D2 难度 · L0–L3（注释上限 600 词/任务，含加分项）

```text
You are designing an alien creature for XenoDesign. Do not ask questions; produce the output directly.

=== WHAT TO PRODUCE ===
For each level requested below, produce one SVG drawing of a single alien creature, followed by a --- separator, followed by a design note. Levels: L0, L1, L2, L3.

=== SVG RULES ===
- viewBox="0 0 512 512"
- One creature only per drawing.
- No <text> elements, no external references, no raster images, under 512 KB.
- L0: full body, side or 3/4 view (creature.svg).
- L1: six orthographic views — front, back, left, right, top, bottom.
- L2: cutaway or cross-section (section.svg).
- L3: skeleton.svg + pelt.svg (see L3 rules below).

=== CONSTRAINT GROUPS AND PRIORITY ===
Constraints are grouped as P (global parameters), F (free design goals), Q (exact counts or prohibitions of repeatable parts), N (body-plan rules). If constraints seem to conflict and cannot coexist, follow P > F > Q > N. If they can coexist with an explanation, keep both and write a RECONCILE line.

=== THE CONSTRAINTS ===
P1: body length 1-3 m.
P2: silicon-based biochemistry.
F1: lives at deep-sea hydrothermal vents.
F2: filter-feeds on spores or suspended particles.
F3: communicates by light patterns.
F4: rolls into a ball for defense.
Q1: exactly 6 limbs.
Q2: exactly 4 eyes.
Q3: exactly 2 feeding openings.
Q4: exactly 2 spore sacs.
Q5: exactly 6 dorsal plates.
Q6: exactly 2 antennae.
N1: exoskeleton.

=== BONUS (independent badges; not constraints) ===
non-humanoid, non-soft, non-earth, non-tentacle-face.

=== L1 RULES ===
Using the same creature as the source, draw six orthographic views: front, back, left, right, top, bottom. One SVG per view. Use the same scale and alignment in every view. No perspective. Keep every count, pattern, and proportion identical across views. If a feature is hidden in one view, it still exists in the design; do not delete it. Do not redesign the creature.

=== L2 RULES ===
Using the same creature as the source, draw a cutaway or cross-section (same viewBox). Choose a plane that shows how the feeding openings connect to a shared digestive cavity, and how the two spore sacs sit. Show the structural material. Do not label the image. Do not redesign the exterior.

=== L3 RULES ===
Using the same creature as the source, draw skeleton.svg: the structural frame with a faint body outline; joints and limbs must align with the exterior; keep the same counts.

Also draw pelt.svg: the skin removed as ONE continuous piece and unfolded flat, like a tiger pelt stretched on the ground. Same viewBox. Show the complete outer surface, the seam/incision lines, and how the pattern continues across them. Treat the skin as a single 2D surface with holes: every feeding opening, eye, limb socket, tail base, and spore-sac opening must appear as a hole, a boundary, or an extension in the sheet. Show the dorsal / ventral / left / right layout and where the seams run. The sheet must be one connected piece, not several pieces laid side by side. Do NOT draw a cutaway. Do NOT draw an exploded view. Do NOT separate the skin into multiple pieces. Do NOT change the creature's counts or pattern.

=== THE DESIGN NOTE ===
- At most 600 words PER TASK (all levels share this cap, not per view).
- One line per constraint, format: P1 -> the visible feature that shows it.
- If a constraint is hidden in this view, say so and where it is.
- Add a RECONCILE line for Q1 (six limbs) and F4 (rolls into a ball): explain how six limbs fold so the body can close into a ball.
- L1+ add a line "Source: L0 <id>".
- L3 add a line "PELT: one continuous sheet; seams ...; holes ...".
- If two constraints conflict, add a CONFLICT line.
- Do not write lore.

=== OUTPUT SHAPE ===
For each level:
SVG
---
Design note

=== SELF-CHECK (8 items) ===
1. One creature only per drawing.
2. viewBox is 0 0 512 512.
3. All counts match the constraints in every view; skeleton and cross-section support them.
4. No <text> in the SVG.
5. One note line per constraint.
6. Drawing and note agree; counts and patterns stay consistent across views.
7. Total note is within 600 words for the whole task.
8. L3 pelt is one continuous flat sheet (not a cutaway, not an exploded view); the RECONCILE line and L1+ Source lines are present.
```

---

## 三、D3 难度 · L0 + L1（注释上限 900 词/任务）

```text
You are designing an alien creature for XenoDesign. Do not ask questions; produce the output directly.

=== WHAT TO PRODUCE ===
For each level requested below, produce one SVG drawing of a single alien creature, followed by a --- separator, followed by a design note. Levels: L0, L1.

=== SVG RULES ===
- viewBox="0 0 512 512"
- One creature only per drawing.
- No <text> elements, no external references, no raster images, under 512 KB.
- L0: full body, side or 3/4 view (creature.svg).
- L1: six orthographic views — front, back, left, right, top, bottom (front.svg ... bottom.svg).

=== CONSTRAINT GROUPS AND PRIORITY ===
Constraints are grouped as P (global parameters), F (free design goals), Q (exact counts or prohibitions of repeatable parts), N (body-plan rules). If constraints seem to conflict and cannot coexist, follow P > F > Q > N. If they can coexist with an explanation, keep both and write a RECONCILE line.

=== THE CONSTRAINTS ===
P1: body length 10-50 m.
P2: ammonia-based biochemistry.
P3: in a dense, corrosive atmosphere.
F1: drifts in a gas giant's clouds.
F2: filter-feeds on spores or suspended particles.
F3: communicates by light patterns.
F4: has a dormant cyst stage.
F5: changes color for camouflage.
F6: builds traps or structures.
Q1: exactly 6 limbs.
Q2: exactly 4 eyes.
Q3: exactly 3 feeding openings.
Q4: exactly 4 gill openings.
Q5: exactly 6 light organs.
Q6: exactly 4 sensory pits.
Q7: exactly 8 body segments.
Q8: exactly 3 body sections.
Q9: no wings.
N1: radial symmetry.
N2: open circulatory system.

=== L1 RULES ===
Using the same creature as the source, draw six orthographic views: front, back, left, right, top, bottom. One SVG per view. Use the same scale and alignment in every view. No perspective. Keep every count, pattern, and proportion identical across views. If a feature is hidden in one view, it still exists in the design; do not delete it. Do not redesign the creature.

=== THE DESIGN NOTE ===
- At most 900 words PER TASK (both levels share this cap, not per view).
- One line per constraint, format: P1 -> the visible feature that shows it.
- If a constraint is hidden in this view, say so and where it is.
- Add a RECONCILE line for Q1 (six limbs) arranged along N1 (radial symmetry): explain how the six limbs, four eyes, six light organs and four sensory pits are distributed around the radial axis, and how Q8 (three body sections) coexists with Q7 (eight body segments) — sections are head/thorax/abdomen-like divisions, segments are repeated units.
- L1 add a line "Source: L0 <id>".
- If two constraints conflict, add a CONFLICT line.
- Do not write lore.

=== OUTPUT SHAPE ===
For each level:
SVG
---
Design note

=== SELF-CHECK (8 items) ===
1. One creature only per drawing.
2. viewBox is 0 0 512 512.
3. All counts match the constraints in every view; counts, proportions, and patterns stay consistent across the six L1 views.
4. No <text> in the SVG.
5. One note line per constraint.
6. Drawing and note agree.
7. Total note is within 900 words for the whole task.
8. Both RECONCILE lines and the L1 Source line are present.
```

---

## 三份卡的关键检查

| 项         | D1                                                  | D2                                                           | D3                                                           |
| ---------- | --------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 配额       | 1P+2F+3Q = 6 条                                     | 2P+4F+6Q+1N = 13 条                                          | 3P+6F+9Q+2N = 20 条                                          |
| 层级       | L0–L4                                               | L0–L3                                                        | L0+L1                                                        |
| 注释上限   | 300 词/任务                                         | 600 词/任务                                                  | 900 词/任务                                                  |
| Tension    | 0                                                   | 1（Q1 六肢 + F4 卷球）                                       | 2（Q1+N1 辐射排列；Q7+Q8 分节/体区）                         |
| 加分项     | 无                                                  | 4 枚徽章                                                     | 无                                                           |
| 互斥组检查 | Q1 触角、Q2 肢体总数、Q3 尾分属不同维度，不重复计数 | Q1 六肢总数未再单列 Q-02 腿；Q3 进食口与 Q4 孢子囊分属 G3 不同维度 | Q3 进食口 / Q4 鳃孔分属 G3；Q7 体节 / Q8 体区分属 G4；Q1 六肢未再单列腿 |
| 死题检查   | F1 冰下 + F2 储水囊可共存；无冲突                   | F1 深海 + F2 过滤 + F3 光通信互补；F4 卷球与 Q1 六肢可解释为 Tension，不是死题 | P3 浓密腐蚀大气 + F1 云层可共存；F5 变色与 F2 过滤无冲突；N2 开管循环需 L2 剖面才可见，L1 注释写 hidden |

其中 D2 的 Tension 写法、D3 的两条 RECONCILE 已直接嵌入提示词，注释里必须给出对应解释行；L3 的 pelt 已按新版要求写成"一张连续皮平铺展开、带孔洞与接缝、明确禁止剖面/爆炸图"，并在自检第 8 项单独设卡。