# ============================================================
# X-DONUT-001 · 完整任务包（L0–L5）
# 难度 D2 · 13 条约束 · 注释上限 600 词/任务 · Tension T-01
# 题眼 Q1：主体上有一个直观占比 ≥ 1/3 的贯穿空腔（甜甜圈拓扑）
# 用法：先跑 §1 L0；§2–§6 按需接在 L0 输出之后追加，复用同一只生物，不重画。
# ============================================================


# ============================================================
# §0 约束卡速查
# ============================================================
# P1  body length 1-3 m
# P2  silicon-based biochemistry
# F1  lives in molten rock
# F2  eats minerals and rocks
# F3  stores heat in a visible dorsal organ
# F4  communicates by vibration
# Q1  one through-hole cavity; visible area >= 1/3 of body silhouette (donut topology)
# Q2  exactly 4 limbs
# Q3  exactly 2 legs
# Q4  exactly 2 manipulators
# Q5  no eyes
# Q6  exactly 3 feeding openings
# N1  no vertebrae (mineral shell/frame)
# 加分项：non-humanoid, non-soft, non-earth
# 优先级：P > F > Q > N
# Tension：T-01（4 肢 = 2 腿 + 2 臂），写 RECONCILE
# 计数：2P + 4F + 6Q + 1N = 13  ->  D2  ->  600 词上限


# ============================================================
# §1 L0 主提示词（完整，可直接粘贴给被测模型）
# ============================================================
You are a xenobiology designer. Do not ask questions. Produce the output directly.

=== WHAT TO PRODUCE ===

One self-contained SVG file named creature.svg, followed by a --- separator,
followed by a design note in plain text.

=== SVG RULES ===

- viewBox="0 0 512 512".
- Full body, side or 3/4 view, one creature only.
- No <text> elements, no external references, no raster images.
- File size under 512 KB.
- The creature must read as a single organism, not a collage.

=== CONSTRAINT GROUPS AND PRIORITY ===

P = global parameter (size, biochemistry, environment).
F = free design goal (habitat, function, organ).
Q = exact count or prohibition of a repeatable part, or a hard geometric ratio.
N = body-plan rule (spine, feet, exoskeleton, symmetry).
Priority when constraints conflict across groups: P > F > Q > N.
If two constraints can coexist with an explanation, keep both and write a RECONCILE line.
If they cannot coexist and are in different groups, follow P > F > Q > N and write a CONFLICT line.
If they cannot coexist and are in the same group, keep the more specific constraint and write a CONFLICT line.

=== BONUS (independent, optional) ===

Aim for: non-humanoid, non-soft, non-earth silhouette.
These are badges, not constraints; do not sacrifice a constraint for a badge.

=== THE CONSTRAINTS ===

P1: body length 1-3 m.
P2: silicon-based biochemistry; the body reads as crystal, mineral, or stone, not flesh.
F1: lives in molten rock.
F2: eats minerals and rocks.
F3: stores heat in a visible dorsal organ.
F4: communicates by vibration.
Q1: the main body has ONE through-hole cavity. Its visible area must be at least one third (1/3) of the body silhouette area, so the creature reads as donut-like topology. The cavity must be a real opening in the body, not a painted spot and not a gap between limbs.
Q2: exactly 4 limbs in total.
Q3: exactly 2 legs.
Q4: exactly 2 manipulators.
Q5: no eyes and no eye-like structures.
Q6: exactly 3 feeding openings.
N1: no vertebrae; the body is supported by a mineral shell or frame, not a spinal column.

RECONCILE (T-01): Q2 = Q3 + Q4. The 4 limbs are exactly 2 legs plus 2 manipulators; the total is the sum of the parts, no extra limbs.

=== THE DESIGN NOTE ===

- At most 600 words. The cap is for this whole task, not per view.
- One line per constraint, in the form:
  P1 -> the visible feature that shows it
- If a constraint is hidden in this view, write "hidden in this view" and say where it is.
- For Q1, state how the 1/3 area ratio is met: describe the cavity outline and compare it to the body silhouette.
- Add a RECONCILE line for T-01.
- Do not write lore, history, or worldbuilding.
- The drawing is primary; the note only maps constraints to visible features.

=== OUTPUT SHAPE ===

<svg ...>...</svg>
---
P1 -> ...
P2 -> ...
...
RECONCILE -> ...

=== SELF-CHECK (8 items) ===

1. One creature only.
2. viewBox is 0 0 512 512.
3. Q1 cavity is visible and reads as at least 1/3 of the body silhouette.
4. Counts match: 4 limbs = 2 legs + 2 manipulators; 3 feeding openings; 0 eyes.
5. No <text> in the SVG.
6. One note line per constraint.
7. Note is at most 600 words.
8. RECONCILE line for T-01 is present.


# ============================================================
# §2 L1 六视图（接在 L0 之后追加）
# ============================================================
Using the same creature as the source, draw six orthographic views:
front, back, left, right, top, bottom.

One SVG per view: front.svg, back.svg, left.svg, right.svg, top.svg, bottom.svg.
Same scale and alignment in every view. No perspective.
Keep every count, pattern, and proportion identical across views.
Q1 must be traceable in at least two views: show where the cavity opens and where it passes through.
If a feature is hidden in one view, it still exists; do not delete it.
Do not redesign the creature.

# L1 注释追加：写 Source: L0 <id>；六视图一致性一句话；Q1 在哪些视图可见、洞的进出口在哪。


# ============================================================
# §3 L2 剖面（接在 L0 之后追加）
# ============================================================
Using the same creature as the source, draw section.svg (same viewBox).

Choose a plane that cuts through the Q1 cavity and shows:
- the cavity as a continuous void inside the body,
- how the 3 feeding openings connect to a shared digestive cavity,
- the mineral shell or frame that replaces the vertebral column.

Do not label the image. Add one note line per internal feature.
Do not redesign the exterior.

# L2 注释追加：Q1 是连续 void；3 个进食口连到同一腔体；N1 矿物架在剖面里可见。


# ============================================================
# §4 L3 骨骼 + 拓扑皮张（接在 L0 之后追加）
# ============================================================
Using the same creature as the source, draw skeleton.svg and pelt.svg (same viewBox).

skeleton.svg: the mineral frame with a faint body outline. Joints and limbs align with the exterior. Same limb count, opening count, and cavity position; do not add or remove any.

pelt.svg: the skin removed as ONE continuous piece and unfolded flat, like a tiger pelt stretched on the ground. Treat the skin as a single 2D surface with holes: the Q1 cavity must appear as a large hole or a tunnel boundary; every feeding opening, limb socket, and tail base must appear as a hole, boundary, or extension. Show dorsal/ventral/left/right layout and where the seams run. The sheet must be one connected piece.
Do NOT draw a cutaway. Do NOT draw an exploded view. Do NOT separate the skin into multiple pieces. Do NOT change counts or pattern.

# L3 注释追加：写 PELT: one continuous sheet; seams...; holes...；Q1 在皮张上是洞/隧道边界；孔洞逐一列出。


# ============================================================
# §5 L4 完整动画（接在 L0 之后追加）
# ============================================================
Using the same creature as the source, animate a full locomotion cycle:
idle -> run -> jump -> land -> idle.

Output motion.svg: one self-contained animated SVG using SMIL or CSS.
Same 512x512 viewBox. Duration 2-4 seconds. Loop seamlessly.

Keep anatomy identical in every frame: same limb count, opening count, cavity size and position, pattern, and proportions.
Show weight, contact, anticipation, and follow-through.
The Q1 cavity must not collapse, teleport, or change area ratio during the cycle.
No limb teleportation, no sliding feet, no changing counts.

If you cannot animate, output 8-12 frames as frame01.svg ... frame12.svg and say so in the note.

# L4 注释追加：写 MOTION: loop Xs; contact...; frames...；Q1 空腔每帧保持面积比与位置。


# ============================================================
# §6 L5 可选彩蛋：骑自行车（接在 L0 之后追加）
# ============================================================
Optional capstone. Using the same creature as the source, show it riding a bicycle (ride.svg, same viewBox).

Draw the bicycle with two wheels, a frame, handlebars, and pedals.
Show the riding relation: the creature is on the bicycle, in contact with the seat and pedals, not floating beside it.
The bicycle is an object, not a second creature.
Keep anatomy and pattern identical to the source; the Q1 cavity must remain readable.
Animate a pedaling/balance cycle, or draw one clear scene.

# L5 注释追加：写 RIDE: bicycle...; contact...；Q1 空腔仍可读。L5 不计入 L0-L4 必做链路，跳过不算失败。


# ============================================================
# §7 层级检查速查
# ============================================================
# L0  creature.svg + design.md
#     核心：Q1 空腔可见且面积 >= 1/3；4 肢 = 2 腿 + 2 臂；3 口；0 眼
# L1  front/back/left/right/top/bottom.svg
#     核心：六视图数量/比例/花纹一致；Q1 在 >=2 个视图可追踪
# L2  section.svg
#     核心：Q1 是连续 void；3 口连同一腔体；N1 矿物架可见
# L3  skeleton.svg + pelt.svg
#     核心：骨架对齐；皮张是一张连续皮；Q1 是洞/隧道边界
# L4  motion.svg 或 frame01-12.svg
#     核心：循环无缝；数量不变；Q1 不塌、不跳、面积比不变
# L5  ride.svg
#     核心：车结构完整；身体接触车；Q1 仍可读（optional）


# ============================================================
# §8 注释上限提醒
# ============================================================
# - 所有层级共用 600 词/任务，不是每视图 600。
# - L1 六视图、L3 双文件、L4 动画，注释都要覆盖新增视图，但总量不超 600。
# - 写不下就压缩；压缩本身是克制测试。
# - 格式：每条约束一行 "ID -> 可见特征"；看不到写 "hidden in this view"；
#   冲突写 CONFLICT；T-01 写 RECONCILE；L1+ 写 Source: L0 <id>。