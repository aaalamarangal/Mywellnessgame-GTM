# Google Sheets Skill

## What this is

A skill file that teaches Claude how to read any person's sheet via the Google Sheets API.
Use this at the start of every > REVIEW session.

---

## Sheet IDs

| Person | Role | Sheet ID |
|---|---|---|
| Shiva | SELF | 1OYnAoSfx5AsYnwwDiBFfNlogwTla0jBRdwGjqaFLiJg |
| Vinotha | TEAM | 1Xy0SYqIIgmqvz7spR1ayPmVyF-FL-t_CRyxkZ9E1kdU |
| Sujith | CLIENT | 12hHoKQlu1T6Iad3mPOJ44knWt7yZuMNpi6DNucFXWh8 |

---

## Three tabs per sheet (Sujith and Vinotha)

| Tab | Stands for | Who fills it | Status |
|---|---|---|---|
| Rev-B | Reviewing Breadth (Acute debt) | The person | Active — read in every REVIEW session |
| Rem-B | Remembering Breadth (Acute debt) | The person | Active — read in every REVIEW session |
| Rec-B | Recognising | Claude (coaching output) | Built through coaching — not an input |

## Six tabs — Shiva only

Shiva has three dimensions of debt, each with a Reviewing and Remembering tab.
Shiva fills all tabs manually. Claude reads and diagnoses patterns.

| Tab | Full name | Debt type | Template |
|---|---|---|---|
| Rev-B | Reviewing Breadth | Acute — work through immediately | Rev-B column map (A–M) |
| Rem-B | Remembering Breadth | Acute | Rem-B column map (A–K) |
| Rev-L | Reviewing Length | Sub-acute — neither acute nor chronic | Same as Rev-B (A–M) |
| Rem-L | Remembering Length | Sub-acute | Same as Rem-B (A–K) |
| Rev-D | Reviewing Depth | Chronic — deep-rooted, long-standing | Same as Rev-B (A–M) |
| Rem-D | Remembering Depth | Chronic | Same as Rem-B (A–K) |

## How to read a sheet

Run this command from the repo root:

```bash
python skills/read_sheet.py <sheet_id> <tab_name>
```

### Read Rev-B tab (acute — planning game)
```bash
python skills/read_sheet.py <sheet_id> "Rev-B"
```

### Read Rem-B tab (acute — reflection game)
```bash
python skills/read_sheet.py <sheet_id> "Rem- B"
```
Note: The tab name has a space — "Rem- B" not "Rem-B". Confirm exact tab name before reading.

### Read Rev-L tab (sub-acute — planning game) — Shiva only
```bash
python skills/read_sheet.py <sheet_id> "Rev-L"
```

### Read Rem-L tab (sub-acute — reflection game) — Shiva only
```bash
python skills/read_sheet.py <sheet_id> "Rem-L"
```

### Read Rev-D tab (chronic — planning game) — Shiva only
```bash
python skills/read_sheet.py <sheet_id> "Rev-D"
```

### Read Rem-D tab (chronic — reflection game) — Shiva only
```bash
python skills/read_sheet.py <sheet_id> "Rem-D"
```

---

## Column Maps

Rev-L, Rev-D use the same column map as Rev-B (A–M).
Rem-L, Rem-D use the same column map as Rem-B (A–K).
The debt type (acute / sub-acute / chronic) determines which tab the row goes in — not the structure.

## Rev-B Column Map (Planning Game — also applies to Rev-L and Rev-D)

| Column | Name | What it means |
|---|---|---|
| A | Situation | The context or trigger |
| B | Date | When logged |
| C | Types of outcome | High / Medium / Low leverage |
| D | Macro outcome | 12-week direction |
| E | Micro outcome | 4-week milestone |
| F | Nano outcome | 1-week target |
| G | Pico outcome | Today's game |
| H | Constraints — credits | Clarity / Action / Lesson |
| I | Constraints — sub-credits | Concepts/Qualities / Tasks/Tactics / Workflows/Capabilities |
| J | Next steps | Specific steps to accomplish Pico today |
| K | Status | Yes / No — assessment done |
| L | Pico progress | Complete / Incomplete |
| M | Journal | PICO reflection — and any shift in Nano/Micro/Macro |

---

## Rem-B Column Map (Reflection Game — also applies to Rem-L and Rem-D)

| Column | Name | What it means |
|---|---|---|
| A | Date | When logged |
| B | High leverage outcome | What they wanted to accomplish |
| C | Diagnostic | Step 1: context/content/formula → Step 2: concept/quality → Step 3: personal/business |
| D | High friction painway | What created friction |
| E | Status | Y / N |
| F | Q1 — What not yet working | Not what happened — what is not working |
| G | Q1a — Learning (didn't work) | What's missing — subtract or divide |
| H | Q1b — Next steps for Q1a | Specific steps only |
| I | Q2 — What's working | Not what happened — what is working |
| J | Q2a — Learning (worked) | What's missing — add or multiply |
| K | Q2b — Next steps for Q2a | Specific steps only |

---

---

## How to write to a sheet (append rows)

Run this command from the repo root:

```bash
python skills/write_sheet.py <sheet_id> <tab_name> '<json_rows>'
```

Where `json_rows` is a JSON array of arrays. Each inner array = one row. Each element = one cell.

### Add a Q&A entry — Open mode (question only, Shiva answers himself)
```bash
python skills/write_sheet.py 1OYnAoSfx5AsYnwwDiBFfNlogwTla0jBRdwGjqaFLiJg "Rewire" '[["8 Mar","Coach","Your question here","","Open"]]'
```

### Add a Q&A entry — Answered mode (question + answer from coaching context)
```bash
python skills/write_sheet.py 1OYnAoSfx5AsYnwwDiBFfNlogwTla0jBRdwGjqaFLiJg "Rewire" '[["8 Mar","Coach","Your question here","Your answer here","Answered"]]'
```
Use Answered mode when the answer is already clear from patterns in client-[name].md or delivery-log.md. Shiva can edit the answer in the sheet anytime.

### Edit an existing row manually
Open the sheet, find the row, type directly in the cell.

---

## Q&A Section — Rewire Tab

Appended at the bottom of the Rewire tab (rows 22–25 on Shiva's sheet).

| Column | Label in Q&A section |
|---|---|
| A | Date |
| B | Asked by |
| C | Question |
| D | Answer |
| E | Status (Open / Answered) |
| F | (unused) |

**Open mode:** Q only, col D blank, col E = "Open". Shiva writes his own answer in the sheet.
**Answered mode:** Q + A both filled from coaching context, col E = "Answered". Shiva confirms or edits.
**To edit any entry:** Open the sheet, type directly in the cell.
**To read all Q&A:** Ask Claude "Read the Q&A section from the Rewire tab."

---

## First-time setup

If the libraries are not installed, run:
```bash
pip install google-auth google-auth-httplib2 google-api-python-client
```

Credentials file: `credentials/relaxedness-website-09b3a51b96a2.json`
Service account: `claude-sheets@relaxedness-website.iam.gserviceaccount.com`
Required permission: **Editor** on each sheet (not just Viewer).
