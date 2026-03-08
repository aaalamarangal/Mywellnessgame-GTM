# 3.Remembering fulfilling demand
Parent: 3.Value delivery- remembering demand | CLAUDE.md

## What this folder is

The fulfilling layer of Value Delivery OS.
It covers what happens after the demo call leads to a yes — onboarding, early client work, and what makes the system stick.

## Three sub-folders

- **1.context/** — coaching-methodology.md (3-step coaching sequence) + client-sujith.md (Founder B + Business A, current games, patterns)
- **2.content/** — delivery-log.md — 12-input Macro → Micro → Nano sessions, tagged by person type / leverage / game
- **3.formula/** — (patterns to be built from delivery entries)

## Status

Active. delivery-log.md is live.
Three person types: Sujith (CLIENT), Shiva (SELF), Vinotha (TEAM).
Tags allow filtering by person, leverage level, and active game.

---

## Task Workflow

### > REVIEW: [name]

Shiva shares: client name (e.g., `> REVIEW: Sujith`)

Claude does:
1. Read `1.context/coaching-methodology.md` — understand the 3-step sequence
2. Read `1.context/client-[name].md` — load the client's current context
3. Pull today's rows from Rev-B (acute planning) — what was planned
4. Pull today's rows from Rem-B (acute reflection) — what actually happened, including journal (column M)
5. Run the 3-step coaching sequence against acute (B) data:
   - Step 1 (Recognise): nano connected to macro? constraint correct? next steps specific?
   - Step 2 (What happened): learning or description? regulate or dysregulate? subtract/divide or add/multiply?
   - Step 3 (Journal): pattern or event? which credit is building?

**For > REVIEW: Shiva only — also read the L and D debt tabs:**

6. Pull today's rows from Rev-L (sub-acute planning) and Rem-L (sub-acute reflection)
7. Run the same 3-step sequence against sub-acute (L) data
8. Pull today's rows from Rev-D (chronic planning) and Rem-D (chronic reflection)
9. Run the same 3-step sequence against chronic (D) data
10. Cross-dimension diagnosis — check all three dimensions together:
    - Same situation appearing in two different debt tabs? → possible misclassification or escalation
    - Pattern healthy in one dimension, unhealthy in another? → surface the contrast
    - Which credit (Clarity / Action / Lesson) is building vs stalling across all three?

**Debt dimensions (Shiva's sheet only — not applicable to Sujith or Vinotha):**
- B tabs (Rev-B / Rem-B) = Acute debt — work through immediately
- L tabs (Rev-L / Rem-L) = Sub-acute debt — neither acute nor chronic, building
- D tabs (Rev-D / Rem-D) = Chronic debt — deep-rooted, long-standing
- Shiva fills all tabs manually. Claude reads and diagnoses healthy and unhealthy patterns.
- All Rev-X tabs use the same column map as Rev-B (A–M). All Rem-X tabs use the same column map as Rem-B (A–K).
- See `skills/google-sheets-skill.md` for read commands and column maps.

**REVIEW output format for Shiva:**
```
ACUTE (Rev-B / Rem-B):
[3-step coaching output]

SUB-ACUTE (Rev-L / Rem-L):
[3-step coaching output]

CHRONIC (Rev-D / Rem-D):
[3-step coaching output]

CROSS-DIMENSION:
[Patterns, escalations, or contrasts across all three]

Credits building:
- Clarity: [assessment]
- Action: [assessment]
- Lesson: [assessment]
```

11. Write new entries to `2.content/delivery-log.md` with correct tags
12. Update `1.context/client-[name].md` if new patterns are emerging
13. Surface key observations in chat — regulation state, credits building, patterns to flag
14. Check if any pattern warrants a Q&A entry to the Rewire tab (Shiva's sheet only):
    - Answer already clear from coaching context → use Answered mode (Q + A pre-filled, Status: Answered)
    - Shiva needs to generate the answer → use Open mode (Q only, Status: Open)
    - Run `write_sheet.py` to append. See `skills/google-sheets-skill.md` for commands.
