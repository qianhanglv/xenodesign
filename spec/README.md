# XenoDesign — Standard

This folder is the written standard that the pilot is testing.

| Document | What it is for |
|---|---|
| [异星生物设计_主标准.md](异星生物设计_主标准.md) | The main standard: P/F/Q/N constraints, D1–D3, L0–L5, checks, anti-contamination. |
| [提示词撰写指南.md](提示词撰写指南.md) | How to turn raw requirement words into a complete prompt, including conflict/tension handling. |
| [提示词素材库.md](提示词素材库.md) | The menu: 7 P, 26 F, 24 Q, 10 N, 6 bonus badges, plus the Tension library. |
| [L0_通用提示词模板.md](L0_通用提示词模板.md) | A copy-paste prompt that a model with no project context can execute. |

The documents are Chinese-first for now; an English translation is a good
first contribution. The prompts themselves are English so they can be used
with any model.

Start with the main standard, then the authoring guide, then the library.

## How to use them together

1. **Pick parts from the library.** It is a menu: choose P/F/Q/N items, or
   write your own words in the same format.
2. **Compile them with the authoring guide.** Its meta-prompt classifies each
   word, normalizes vague wording, checks conflicts/tensions, sets the
   difficulty and note cap, and writes the complete prompt.
3. **Use the L0 template as the output skeleton.** The guide fills it; you do
   not need to invent the SVG rules again.
4. **Add new vocabulary at the end of the library.** Give it a new ID, define
   the visual evidence, and mark its minimum level and conflicts. Do not
   renumber existing IDs.

**The library is not a closed list.** The pilot ships 7 P / 26 F / 24 Q / 10 N
/ 6 bonus items; you can add your own P/F/Q/N items as long as they are
visible, countable, or checkable.
