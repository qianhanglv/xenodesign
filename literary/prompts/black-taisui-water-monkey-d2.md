# XenoDesign · 黑太岁 / 水猴子 · D2 完整提示词

用途：B站/抖音“文字里的怪物”系列。  
两只都做成 **D2（90 分，600 词/任务）**，L0–L3。  
`[CANON]` 是原文/百科可考特征；`[INFERRED]` 是为了补全解剖、达到 D2 的设计选择，不是原著断言。

> **皮肤展开修正**：旧提示词只写“one continuous sheet + holes for eyes/limbs/tail”，没有要求头/颈；模型很容易画成“无头躯干皮”。  
> 这两份提示词都明确要求：**有头就带头/颈；无头就写 `HEAD: none by canon` / `HEAD: none in this design`**，不能把“忘画头”混成“无头”。

---

# 1. 黑太岁（《道诡异仙》）

## 可考特征

- 出处：《道诡异仙》丹阳子/黑太岁段落。
- 巨大蛆虫状身体，表面布满粘液。
- 身体覆盖细长触须，生有散发臭气的孔洞。
- 被切下的肢体仍能蠕动；死亡时身体逐渐缩小并渗出粘液。
- 生命力顽强；可蚕食/夺舍；心素口服可压制幻觉，但有被夺舍风险。
- 没有官方固定视觉；同人图不能当参考。
- 来源：[百度百科：道诡异仙/黑太岁描述](https://wapbaike.baidu.com/item/道诡异仙/60978835)

## D2 卡（2P + 4F + 6Q + 1N = 90 分）

| ID | 内容 | 标签 |
|---|---|---|
| P1 | 巨大软体，至少 3 m 宽（尺度为设计推断） | `[INFERRED scale]` |
| P2 | 湿滑粘液表面，无硬壳 | `[CANON]` |
| F1 | 散发臭气的孔洞 | `[CANON]` |
| F2 | 切下的肢体仍会动 | `[CANON]` |
| F3 | 可蚕食/夺舍宿主 | `[CANON]` |
| F4 | 死亡时缩小、渗液 | `[CANON]` |
| Q1 | 恰好 0 根骨头/脊椎 | `[INFERRED]` |
| Q2 | 恰好 0 只眼睛 | `[INFERRED]` |
| Q3 | 除触须外，恰好 0 条肢体 | `[INFERRED]` |
| Q4 | 恰好 1 团主体 | `[CANON]` |
| Q5 | 至少 12 条细触须 | `[INFERRED]` |
| Q6 | 恰好 0 个头 | `[INFERRED]` |
| N1 | 无定形软体，无骨架 | `[INFERRED]` |

## 完整提示词（复制给被测模型）

```text
You are a xenobiology designer. Do not ask questions. Produce the complete file set directly.

=== SOURCE / CANON ===
This is a text-only fan design based on the "Black Tai Sui" (黑太岁) from the Chinese
web novel Dao of the Bizarre Immortal.
[CANON] = explicit in the source or its encyclopedia entry.
[INFERRED] = a design choice added to complete the anatomy; it is not a claim about
the original. Keep these tags in the notes.
Do not use any existing film/anime/fan-art reference.

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
  file, one file at a time.

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
P1 [INFERRED scale]: one huge soft mass, at least 3 m across.
P2 [CANON]: wet, slime-covered surface; no hard shell.

F1 [CANON]: stink-pore openings release a foul odor.
F2 [CANON]: cut-off pieces still move.
F3 [CANON]: it can consume/possess a host.
F4 [CANON]: when it dies, it shrinks and leaks slime.

Q1 [INFERRED]: exactly 0 bones and 0 vertebrae.
Q2 [INFERRED]: exactly 0 eyes.
Q3 [INFERRED]: exactly 0 limbs other than the tentacles.
Q4 [CANON]: exactly 1 body mass.
Q5 [INFERRED]: at least 12 thin tentacles.
Q6 [INFERRED]: exactly 0 heads.

N1 [INFERRED]: amorphous soft body; no skeleton.

=== LEVEL INSTRUCTIONS ===
L0: one 3/4 view; show the single soft mass, the tentacles, and at least 3 stink pores.
L1: six orthographic views. The same 1 body mass and the same tentacle set must be
traceable; no head, no eyes, no limbs, no bones.
L2: one section through the mass; show a central cavity, the stink-pore channels,
and the tentacle canals. No skull, no vertebral column. Mark the inferred anatomy.
L3: skeleton.svg + pelt.svg.
- skeleton: there is no bony skeleton; draw a soft hydrostatic/fibrous frame:
  a root ring for the tentacles and a mesh of fluid sacs. Mark it [INFERRED].
- pelt: ONE continuous sheet, unfolded flat. This creature has NO head:
  write "HEAD: none in this design" in the note and do not invent one.
  The pelt must have: tentacle sleeves (at least 12), stink-pore holes (at least 3),
  no eye holes, no head hole, no limb holes. Wet mottling must continue across
  every seam. This is a topological surface, not a cutaway, not an exploded view,
  not multiple pieces.

=== THE DESIGN NOTE ===
- At most 600 words per note file.
- One line per constraint:
  P1 [INFERRED] -> the visible feature that shows it
- If hidden, write "hidden in this view" and where it is.
- For Q4/Q5, state the single mass and the tentacle count.
- For L1+, write "Source: L0 <id>" and confirm the same counts.
- For L3, write "PELT: one continuous sheet; HEAD: none in this design; ...".
- Do not write lore, history, or a story.

=== OUTPUT ===
Complete file tree + manifest.md with file path | level | note word count |
Source: L0 <id> | [CANON]/[INFERRED] counts.

=== SELF-CHECK (8) ===
1. One creature; one soft body mass.
2. viewBox 512; no text/image/script/external refs.
3. 0 eyes, 0 heads, 0 bones, 0 limbs other than tentacles.
4. At least 12 tentacles and at least 3 stink pores.
5. Every constraint has one note line.
6. The pelt is one continuous sheet with HEAD: none in this design.
7. No note exceeds 600 words.
8. No lore.
```

---

# 2. 水猴子（《道诡异仙》）

## 可考特征

- 出处：《道诡异仙》第 384 章首次提及；第 810/803 章被李火旺斩杀。
- 水栖邪祟，群居。
- 身体长满黑色长毛；手脚像水藻一样扭动。
- 能听懂人话；会袭击过往船只。
- 部分水猴子脸上贴有鳞片。
- 没有官方固定视觉；同人图不能当参考。
- 来源：[百度百科：水猴子](https://baike.baidu.com/item/水猴子/64903377)

## D2 卡（2P + 4F + 6Q + 1N = 90 分）

| ID | 内容 | 标签 |
|---|---|---|
| P1 | 水栖、河/湖环境 | `[CANON]` |
| P2 | 体长约等于人类（尺度为设计推断） | `[INFERRED scale]` |
| F1 | 能听懂人话 | `[CANON]` |
| F2 | 袭击过往船只 | `[CANON]` |
| F3 | 黑色长毛、水藻状手脚 | `[CANON]` |
| F4 | 群居 | `[CANON]` |
| Q1 | 恰好 4 条肢体 | `[INFERRED]` |
| Q2 | 恰好 1 个头 | `[INFERRED]` |
| Q3 | 恰好 2 只眼 | `[INFERRED]` |
| Q4 | 恰好 0 条尾巴 | `[INFERRED]` |
| Q5 | 恰好 0 只翅膀 | `[INFERRED]` |
| Q6 | 恰好 0 只角 | `[INFERRED]` |
| N1 | 四足/人形身体规划 | `[INFERRED]` |

## 完整提示词（复制给被测模型）

```text
You are a xenobiology designer. Do not ask questions. Produce the complete file set directly.

=== SOURCE / CANON ===
This is a text-only fan design based on the "water monkey" (水猴子) from the Chinese
web novel Dao of the Bizarre Immortal.
[CANON] = explicit in the source or its encyclopedia entry.
[INFERRED] = a design choice added to complete the anatomy; it is not a claim about
the original. Keep these tags in the notes.
Do not use any existing film/anime/fan-art reference.

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
  file, one file at a time.

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
P1 [CANON]: aquatic; lives in rivers/lakes.
P2 [INFERRED scale]: roughly human-sized.

F1 [CANON]: it understands human speech.
F2 [CANON]: it attacks passing boats.
F3 [CANON]: black long hair; hands and feet move like water weeds.
F4 [CANON]: it lives in groups.

Q1 [INFERRED]: exactly 4 limbs.
Q2 [INFERRED]: exactly 1 head.
Q3 [INFERRED]: exactly 2 eyes.
Q4 [INFERRED]: exactly 0 tails.
Q5 [INFERRED]: exactly 0 wings.
Q6 [INFERRED]: exactly 0 horns.

N1 [INFERRED]: a four-limbed, humanoid body plan.

=== LEVEL INSTRUCTIONS ===
L0: one 3/4 view; show the head, black hair, water-weed limbs, and 4 limbs.
L1: six orthographic views. 1 head, 2 eyes, 4 limbs, 0 tail must be traceable.
L2: one section through the head/neck/torso; show the shared cavity and the
water-weed limb canals. Mark the inferred anatomy.
L3: skeleton.svg + pelt.svg.
- skeleton: a four-limbed frame with a head/neck; no tail, no wings, no horns.
- pelt: ONE continuous sheet, unfolded flat. The pelt MUST include the head and
  neck as part of the same sheet: the head/face is a front lobe; the neck is a
  continuous bridge to the torso; do not omit the head, do not draw a separate
  head/mask, and do not replace the head with a hole. Eye sockets, mouth openings,
  and ear holes sit on the head lobe. The sheet must have: 4 limb sleeves,
  1 head opening, no tail hole, no wing holes, no horn holes. The black hair-line
  / follicle pattern must continue across every seam. This is a topological
  surface, not a cutaway, not an exploded view, not multiple pieces.

=== THE DESIGN NOTE ===
- At most 600 words per note file.
- One line per constraint:
  P1 [CANON] -> the visible feature that shows it
- If hidden, write "hidden in this view" and where it is.
- For Q1/Q2/Q3, state counts and where they are visible.
- For L1+, write "Source: L0 <id>" and confirm the same counts.
- For L3, write "PELT: one continuous sheet; HEAD/NECK: 1 head attached; ...".
- Do not write lore, history, or a story.

=== OUTPUT ===
Complete file tree + manifest.md with file path | level | note word count |
Source: L0 <id> | [CANON]/[INFERRED] counts.

=== SELF-CHECK (8) ===
1. One creature; 1 head, 2 eyes, 4 limbs, 0 tail, 0 wings, 0 horns.
2. viewBox 512; no text/image/script/external refs.
3. Black hair and water-weed limbs are readable.
4. Every constraint has one note line.
5. The pelt is one continuous sheet with an attached head/neck and 4 limb sleeves.
6. No detached head/mask; no headless torso sheet.
7. No note exceeds 600 words.
8. No lore.
```

---

# 使用提示

- 两只都按 **D2 / 90 分 / 600 词** 写；`[INFERRED]` 是为了补全解剖，不是原著断言。
- 黑太岁：无头、无眼、无骨、无定形；皮张必须写 `HEAD: none in this design`，不要补一个头。
- 水猴子：有头/颈/四足；皮张必须把头/颈连在同一张皮上，不能画成无头躯干皮或单独面具。
- 目标模型必须在 note 里保留 `[CANON]` / `[INFERRED]` 标签；评审时只看 `[CANON]` 是否对得上原文。
- 不要给模型看电影/动画/同人图；这是文字到 3D 的测试。
