# XenoDesign · 三只文学生物 · D2 完整提示词

用途：B站/抖音“文字里的怪物”系列。  
每只生物都做成 **D2（90 分，600 词/任务）**；`[CANON]` 是原文可考特征，`[INFERRED]` 是为了达到 D2 而补的**设计选择**，不是原著断言。

- 水中监视者：L0–L3
- Runespoor：L0–L3
- 羽蛇：L0–**L4**（三只中选它做 L4；其余到 L3）

这三个提示词都可以直接复制给被测模型。  
输出要求：完整 SVG/MD 文件，按 L 层级放文件夹；聊天界面不能建文件时，用“路径 + 完整代码块”。

---

# 1. 水中监视者（Watcher in the Water）

## 可考特征

- 出处：《魔戒》第一部，第二卷第四章 “A Journey in the Dark”。
- **至少 21 条触手**；电影版只出现 12 条，且没有完整身体。
- 触手绿色、会发光、像手指一样灵活。
- 身体、头、骨骼、内部结构都没有描述；托尔金只给了“触手”和“黑湖”。
- 它是摩瑞亚西门黑湖里的伏击者，会抓取靠近水边的目标。
- 来源：[CBR：原著 21 条触手 vs 电影 12 条](https://www.cbr.com/lord-of-rings-watcher-water-kraken/)；[中文维基：绿色发光触手、身体不明](https://zh.wikipedia.org/wiki/水中監視者)

## D2 卡（2P + 4F + 6Q + 1N = 90 分）

| ID | 内容 | 标签 |
|---|---|---|
| P1 | 摩瑞亚西门外的黑湖 | `[CANON]` |
| P2 | 古老、来源不明，早于半兽人 | `[CANON]` |
| F1 | 水下伏击 | `[CANON]` |
| F2 | 触手抓取、拖拽猎物 | `[CANON]` |
| F3 | 封住摩瑞亚西门 | `[CANON]` |
| F4 | 触手绿色、发光、指尖状 | `[CANON]` |
| Q1 | 恰好 21 条触手 | `[CANON]` |
| Q2 | 恰好 0 只可见眼睛 | `[INFERRED]` |
| Q3 | 恰好 0 个可见头部 | `[INFERRED]` |
| Q4 | 除触手外，恰好 0 条肢体 | `[INFERRED]` |
| Q5 | L0 中恰好 1 团主体露出水面 | `[INFERRED]` |
| Q6 | L0 中至少 3 条触手破水 | `[INFERRED]` |
| N1 | 无内骨骼、无脊椎 | `[INFERRED]` |

## 完整提示词（复制给被测模型）

```text
You are a xenobiology designer. Do not ask questions. Produce the complete file set directly.

=== SOURCE / CANON ===
This is a text-only fan design based on the Watcher in the Water from
The Lord of the Rings, Book II, Chapter 4 ("A Journey in the Dark").
[CANON] = explicit in the source or its official companion material.
[INFERRED] = a design choice added to make a complete creature; it is not a claim
about the original text. Keep these tags in the notes.

=== WHAT TO PRODUCE ===
The requested levels: L0, L1, L2, L3. Do not add L4/L5.
Create complete files, one folder per level:

L0/creature.svg
L0/design.md
L1/front.svg
L1/back.svg
L1/left.svg
L1/right.svg
L1/top.svg
L1/bottom.svg
L1/note.md
L2/section.svg
L2/note.md
L3/skeleton.svg
L3/pelt.svg
L3/note.md
manifest.md

Each note must be at most 600 words. Do not pad.

=== SVG RULES ===
- viewBox="0 0 512 512".
- Full body, one creature only, side or 3/4 view at L0.
- No <text>, no <image>, no <script>, no foreignObject, no external href.
- File size under 512 KB.
- The creature must read as one organism, not a collage.
- If the interface cannot create files: output "path + complete code block" for each
  file, one file at a time. Do not merge all files into one block.

=== CONSTRAINT GROUPS AND PRIORITY ===
P = global parameter.
F = free design goal.
Q = exact count, prohibition, or hard geometric ratio.
N = body-plan rule.
Priority when constraints conflict across groups: P > F > Q > N.
If two constraints can coexist, keep both and write RECONCILE.
If they cannot coexist and are in different groups, follow P > F > Q > N and
write CONFLICT.
If they cannot coexist and are in the same group, keep the more specific one and
write CONFLICT.

=== BONUS (optional, all levels) ===
Aim for: non-humanoid, non-earth, non-cliche.
These are badges, not constraints; do not sacrifice a constraint for a badge.

=== THE CONSTRAINTS ===
P1 [CANON]: a dark freshwater lake at the West-gate of Moria.
P2 [CANON]: ancient and of unknown origin, older than the orcs.
F1 [CANON]: ambush predator; it waits still in the water.
F2 [CANON]: it grasps and drags prey with its tentacles.
F3 [CANON]: it can block the gate; its arms reach across the entrance.
F4 [CANON]: its tentacles are green, faintly glowing, and finger-like at the tips.

Q1 [CANON]: exactly 21 tentacles. Count them; no more, no fewer.
Q2 [INFERRED]: exactly 0 visible eyes. Do not paint eye-like spots.
Q3 [INFERRED]: exactly 0 visible heads. The body is a mass, not a head.
Q4 [INFERRED]: exactly 0 limbs other than the 21 tentacles.
Q5 [INFERRED]: exactly 1 body mass breaks the water surface in L0.
Q6 [INFERRED]: at least 3 tentacles break the water surface in L0.

N1 [INFERRED]: no endoskeleton and no vertebral column; the body is a soft mass
supported by fluid pressure.

=== LEVEL INSTRUCTIONS ===
L0: one 3/4 view; show the body mass and the 21 tentacles clearly enough to count.
L1: six orthographic views. The same 21 tentacles must be traceable; no extra
tentacle appears in any view. Use dashed lines only for occluded tentacles.
L2: one section through the body mass; show a central cavity and 21 tentacle
canals. There is no head and no skull. Mark the inferred body plan as [INFERRED].
L3: skeleton.svg + pelt.svg.
- skeleton: a soft hydrostatic body plan; no bones, no vertebrae; show the
  tentacle root ring and the 21 canals.
- pelt: ONE continuous sheet, unfolded flat, like a tiger pelt. It must have:
  exactly 21 tentacle sleeves or holes, one central body opening, no head hole,
  no limb holes. Green photophore speckles cross the seams continuously.
  This is a topological surface, not a cutaway, not an exploded view, not
  multiple pieces.

=== THE DESIGN NOTE ===
- At most 600 words per note file.
- One line per constraint, in the form:
  P1 [CANON] -> the visible feature that shows it
- If a constraint is hidden in this view, write "hidden in this view" and say
  where it is.
- For Q1, state the count and where each tentacle is visible.
- For L1+, write "Source: L0 <id>" and confirm the same 21 tentacles.
- For L3, write "PELT: one continuous sheet; HEAD: none by canon; 21 tentacle sleeves; ...".
- Do not write lore, history, or a story.

=== OUTPUT ===
Output the complete file tree above, plus manifest.md with:
file path | level | note word count | Source: L0 <id> | [CANON]/[INFERRED] counts.
If a constraint is hidden, say so; do not invent a feature that is not in the
constraints.

=== SELF-CHECK (8) ===
1. One creature; one body mass.
2. viewBox 512; no text/image/script/external refs.
3. Exactly 21 tentacles in every view.
4. 0 eyes, 0 heads, 0 limbs other than tentacles.
5. Every constraint has one note line.
6. The pelt is one continuous sheet with 21 tentacle sleeves and "HEAD: none by canon".
7. No note exceeds 600 words.
8. No lore; the drawing is primary.
```

---

# 2. Runespoor（三头蛇）

## 可考特征

- 出处：《神奇动物在哪里》教科书 A–Z 条目。
- 三个头；分别承担 **planner / dreamer / critic** 三种角色。
- 常见长度 **6–7 英尺**；橙黑条纹。
- 原产布基纳法索；黑巫师喜欢养。
- 电影只有删减片段，没有稳定的正片全身设计；教科书文本是主依据。
- 来源：[Wizarding World：三个头的角色](https://www.harrypotter.com/patronus/runespoor)；[Fandom：6–7 ft、橙黑条纹、布基纳法索](https://harrypotter.fandom.com/wiki/Runespoor)

## D2 卡（2P + 4F + 6Q + 1N = 90 分）

| ID | 内容 | 标签 |
|---|---|---|
| P1 | 6–7 英尺长 | `[CANON]` |
| P2 | 布基纳法索的森林 | `[CANON]` |
| F1 | 三个头分别计划/做梦/批评 | `[CANON]` |
| F2 | 黑巫师的宠物 | `[CANON]` |
| F3 | 橙黑条纹 | `[CANON]` |
| F4 | 三个头会半独立行动 | `[CANON]` |
| Q1 | 恰好 3 个头 | `[CANON]` |
| Q2 | 恰好 1 条尾巴 | `[INFERRED]` |
| Q3 | 恰好 0 条肢体 | `[INFERRED]` |
| Q4 | 恰好 0 只翅膀 | `[INFERRED]` |
| Q5 | 每个头恰好 2 只眼 | `[INFERRED]` |
| Q6 | 恰好 1 个身体 | `[CANON]` |
| N1 | 蛇形身体，无腿 | `[CANON]` |

## 完整提示词（复制给被测模型）

```text
You are a xenobiology designer. Do not ask questions. Produce the complete file set directly.

=== SOURCE / CANON ===
This is a text-only fan design based on the Runespoor from the Harry Potter
companion book Fantastic Beasts and Where to Find Them.
[CANON] = explicit in the textbook/official companion.
[INFERRED] = a design choice added to complete the anatomy; not a claim about
the original. Keep these tags in the notes.

=== WHAT TO PRODUCE ===
The requested levels: L0, L1, L2, L3. Do not add L4/L5.
Create complete files, one folder per level:

L0/creature.svg
L0/design.md
L1/front.svg
L1/back.svg
L1/left.svg
L1/right.svg
L1/top.svg
L1/bottom.svg
L1/note.md
L2/section.svg
L2/note.md
L3/skeleton.svg
L3/pelt.svg
L3/note.md
manifest.md

Each note must be at most 600 words. Do not pad.

=== SVG RULES ===
- viewBox="0 0 512 512".
- Full body, one creature only, side or 3/4 view at L0.
- No <text>, no <image>, no <script>, no foreignObject, no external href.
- File size under 512 KB.
- The creature must read as one organism, not a collage.
- If the interface cannot create files: output "path + complete code block" for
  each file, one file at a time.

=== CONSTRAINT GROUPS AND PRIORITY ===
P = global parameter.
F = free design goal.
Q = exact count, prohibition, or hard geometric ratio.
N = body-plan rule.
Priority: P > F > Q > N.
If two constraints can coexist, keep both and write RECONCILE.
If they cannot coexist and are in different groups, follow P > F > Q > N and
write CONFLICT.
If they cannot coexist and are in the same group, keep the more specific one and
write CONFLICT.

=== BONUS (optional, all levels) ===
Aim for: non-humanoid, non-earth, non-cliche.
These are badges, not constraints.

=== THE CONSTRAINTS ===
P1 [CANON]: 6-7 feet long from snout to tail tip.
P2 [CANON]: native to the forests of Burkina Faso.
F1 [CANON]: three heads with three roles: the left head plans, the middle head
dreams, the right head criticizes.
F2 [CANON]: popular with Dark wizards; it reads as an intimidating pet.
F3 [CANON]: orange and black stripes.
F4 [CANON]: the three heads can act semi-independently; they do not all face the
same direction all the time.

Q1 [CANON]: exactly 3 heads.
Q2 [INFERRED]: exactly 1 tail.
Q3 [INFERRED]: exactly 0 limbs.
Q4 [INFERRED]: exactly 0 wings.
Q5 [INFERRED]: exactly 2 eyes on each head; total 6 eyes.
Q6 [CANON]: exactly 1 body.

N1 [CANON]: serpentine body plan; no legs.

=== LEVEL INSTRUCTIONS ===
L0: one 3/4 view; all three heads visible and readable as separate heads.
L1: six orthographic views. Three heads and one tail must be traceable in every
view; no fourth head, no limbs, no wings.
L2: one section through the shared body; show three necks joining one body, one
shared gut, one tail. The three necks are [INFERRED] anatomy; mark them.
L3: skeleton.svg + pelt.svg.
- skeleton: a serpentine frame with three skulls/neck arches and one tail;
  no limbs, no wings.
- pelt: ONE continuous sheet, unfolded flat. It must have:
  exactly 3 head/neck holes, exactly 1 tail opening, no limb holes, no wing holes.
  The orange/black stripes must continue across every seam. This is a topological
  surface, not a cutaway, not an exploded view, not multiple pieces.
  The pelt MUST include the three heads and necks as part of the same sheet:
  each head is a front lobe, each neck a continuous bridge to the shared torso.
  Do not omit the heads, do not draw three separate masks, and do not replace a
  head with a hole.

=== THE DESIGN NOTE ===
- At most 600 words per note file.
- One line per constraint:
  P1 [CANON] -> the visible feature that shows it
- If hidden, write "hidden in this view" and where it is.
- For Q1, state the three heads and their roles.
- For L1+, write "Source: L0 <id>" and confirm the same 3 heads / 1 tail.
- For L3, write "PELT: one continuous sheet; HEAD/NECK: 3 heads attached; 3 head holes; 1 tail opening; ...".
- Do not write lore or a story.

=== OUTPUT ===
Complete file tree + manifest.md with file path | level | note word count |
Source: L0 <id> | [CANON]/[INFERRED] counts.

=== SELF-CHECK (8) ===
1. One creature; one body.
2. viewBox 512; no text/image/script/external refs.
3. Exactly 3 heads, 1 tail, 0 limbs, 0 wings.
4. 2 eyes per head in every view (6 total).
5. Every constraint has one note line.
6. The pelt is one continuous sheet with 3 attached heads/necks (not separate masks), 3 head holes, and 1 tail opening.
7. No note exceeds 600 words.
8. No lore.
```

---

# 3. 羽蛇（《诡秘之主》）

## 可考特征

- 出处：《诡秘之主》阿兹克陵寝段落（读者转载；B 级考据，录前请核对原文章节）。
- 通体覆盖**阴绿显黑的巨大鳞片**。
- 鳞片缝隙长出**洁白的羽毛**；每片鳞/每根羽毛上有不同形状的**奇异符号**。
- 眼窝燃烧**苍白的火焰**；背后有一对**夸张厚实的羽翼**。
- 能喷出覆盖整座陵寝的**苍白之焰**；看见它的人会血肉腐烂、变成活尸。
- 是南大陆神话里的“羽蛇神”，也是死神途径的神话生物形态。
- 来源：[《诡秘之主》羽蛇段落转载](https://blog.csdn.net/qq_40303205/article/details/81216687)（读者转载；B 级）

## D2 卡（2P + 4F + 6Q + 1N = 90 分）

| ID | 内容 | 标签 |
|---|---|---|
| P1 | 巨大到能盘踞陵寝上空（至少 20 m，尺度为设计推断） | `[INFERRED scale]` |
| P2 | 死亡/冥界领域的神话生物 | `[CANON]` |
| F1 | 喷吐苍白之焰 | `[CANON]` |
| F2 | 鳞/羽上的符号使观者腐烂、化为活尸 | `[CANON]` |
| F3 | 死亡的象征/预兆 | `[CANON]` |
| F4 | 阴绿黑鳞 + 白色羽毛的混合表面 | `[CANON]` |
| Q1 | 恰好 2 只翅膀 | `[CANON]` |
| Q2 | 恰好 1 个头 | `[INFERRED]` |
| Q3 | 恰好 2 只眼 | `[CANON]`（眼窝苍白火） |
| Q4 | 恰好 1 条尾巴 | `[INFERRED]` |
| Q5 | 恰好 0 条腿 | `[INFERRED]` |
| Q6 | 恰好 0 只角 | `[INFERRED]` |
| N1 | 蛇形躯干，翼从肩后伸出 | `[INFERRED]` |

## 完整提示词（复制给被测模型）

```text
You are a xenobiology designer. Do not ask questions. Produce the complete file set directly.

=== SOURCE / CANON ===
This is a text-only fan design based on the "feathered serpent" (羽蛇) form in
Lord of the Mysteries. The source describes a huge serpent covered in dark
green-black scales, with white feathers in the gaps, symbols on every scale and
feather, pale flame in the eye sockets, and a pair of huge wings.
[CANON] = explicit in the source passage.
[INFERRED] = a design choice added to complete the anatomy; not a claim about
the original. Keep these tags in the notes.
This is a fan design; do not use any existing film/anime/fan-art reference.

=== WHAT TO PRODUCE ===
The requested levels: L0, L1, L2, L3, L4.
Create complete files, one folder per level:

L0/creature.svg
L0/design.md
L1/front.svg
L1/back.svg
L1/left.svg
L1/right.svg
L1/top.svg
L1/bottom.svg
L1/note.md
L2/section.svg
L2/note.md
L3/skeleton.svg
L3/pelt.svg
L3/note.md
L4/motion.svg
L4/note.md
manifest.md

Each note must be at most 600 words. Do not pad.

=== SVG RULES ===
- viewBox="0 0 512 512".
- Full body, one creature only, side or 3/4 view at L0.
- No <text>, no <image>, no <script>, no foreignObject, no external href.
- File size under 512 KB.
- The creature must read as one organism, not a collage.
- If the interface cannot create files: output "path + complete code block" for
  each file, one file at a time.

=== CONSTRAINT GROUPS AND PRIORITY ===
P = global parameter.
F = free design goal.
Q = exact count, prohibition, or hard geometric ratio.
N = body-plan rule.
Priority: P > F > Q > N.
If two constraints can coexist, keep both and write RECONCILE.
If they cannot coexist and are in different groups, follow P > F > Q > N and
write CONFLICT.
If they cannot coexist and are in the same group, keep the more specific one and
write CONFLICT.

=== BONUS (optional, all levels) ===
Aim for: non-humanoid, non-earth, non-cliche.
These are badges, not constraints; do not sacrifice a constraint for a badge.

=== THE CONSTRAINTS ===
P1 [INFERRED scale]: huge; at least 20 m from snout to tail tip, able to coil
over a mausoleum.
P2 [CANON]: a death/underworld mythic being; it is a symbol of death.

F1 [CANON]: it breathes pale flame that can cover a large building.
F2 [CANON]: the symbols on its scales/feathers rot flesh; seeing it can turn a
viewer into a walking corpse.
F3 [CANON]: it is an omen/symbol of death.
F4 [CANON]: the surface is dark green-black scales with white feathers growing
from the gaps.

Q1 [CANON]: exactly 2 wings.
Q2 [INFERRED]: exactly 1 head.
Q3 [CANON]: exactly 2 eyes, with pale flame in the sockets.
Q4 [INFERRED]: exactly 1 tail.
Q5 [INFERRED]: exactly 0 legs.
Q6 [INFERRED]: exactly 0 horns.

N1 [INFERRED]: a serpentine trunk; the two wings attach behind the shoulders,
not on the head.

=== LEVEL INSTRUCTIONS ===
L0: one 3/4 view; show the 2 wings, 1 head, 2 pale-flame eyes, 1 tail, and the
scale/feather transition.
L1: six orthographic views. 2 wings, 1 head, 2 eyes, 1 tail must be traceable;
no legs, no horns. The symbols must stay on the same body regions.
L2: one section through the trunk and wing roots; show the flame organ and the
symbol channels. The wing roots and flame organ are [INFERRED] anatomy.
L3: skeleton.svg + pelt.svg.
- skeleton: a serpentine frame with two wing girdles and one tail; no legs,
  no horns. Mark the inferred girdles.
- pelt: ONE continuous sheet, unfolded flat. It must have:
  exactly 1 head opening, exactly 2 wing sleeves, exactly 1 tail opening,
  no leg holes, no horn holes. Dark green-black scale fields and white feather
  fields must continue across every seam; the symbols must stay attached to the
  same scale/feather regions. This is a topological surface, not a cutaway, not
  an exploded view, not multiple pieces.
  The pelt MUST include the head and neck as part of the same sheet: the
  head/face is a front lobe; the neck is a continuous bridge to the torso.
  Do not omit the head, do not draw a separate head/mask, and do not replace
  the head with a hole.
L4: motion.svg, a self-contained SMIL animation, 512 x 512, 3.2 s seamless loop.
This is an aerial locomotion variant, with the same rigor as idle->run->jump->
land->idle:
idle hover -> downstroke -> climb -> glide -> land -> idle.
- 20 keyframes; the last keyframe equals the first.
- 2 wings, 1 head, 2 eyes, 1 tail, 0 legs, 0 horns in every frame.
- The scale/feather fields and symbols do not slide, flip, or change count.
- The body does not squash into a different creature.
- Contact: the landing frame has a clear ground contact; no foot sliding (there
  are no feet; the tail/lower body touches down).
- No script, no external file.

=== THE DESIGN NOTE ===
- At most 600 words per note file.
- One line per constraint:
  P1 [INFERRED] -> the visible feature that shows it
- If hidden, write "hidden in this view" and where it is.
- For Q1/Q2/Q3/Q4, state the count and where each is visible.
- For L1+, write "Source: L0 <id>" and confirm the same counts.
- For L3, write "PELT: one continuous sheet; HEAD/NECK: 1 head attached; 1 head opening; 2 wing sleeves; ...".
- For L4, write "MOTION: 3.2 s loop; 20 keyframes; ...".
- Do not write lore, history, or a story.

=== OUTPUT ===
Complete file tree + manifest.md with file path | level | note word count |
Source: L0 <id> | [CANON]/[INFERRED] counts.

=== SELF-CHECK (8) ===
1. One creature; 1 head, 2 wings, 1 tail, 0 legs, 0 horns.
2. viewBox 512; no text/image/script/external refs.
3. 2 eyes with pale flame; symbols remain on the same regions.
4. Every constraint has one note line.
5. The pelt is one continuous sheet with an attached head/neck, 1 head opening, and 2 wing sleeves.
6. L4 loops seamlessly; counts do not change; landing contact is readable.
7. No note exceeds 600 words.
8. No lore.
```

---

# 使用提示

- 三只都按 **D2 / 90 分 / 600 词** 写；`[INFERRED]` 是为了让卡达到 D2 的补全，不是原著断言。
- 水中监视者和 Runespoor 到 **L3**；羽蛇到 **L4**（飞行循环，按 L4 同等严格度）。
- 目标模型必须在 note 里保留 `[CANON]` / `[INFERRED]` 标签；评审时只看 `[CANON]` 是否对得上原文。
- 不要给模型看电影/动画/同人图；这是文字到 3D 的测试。
- 羽蛇的考据是 B 级（读者转载）；录视频前请对照原文章节。
