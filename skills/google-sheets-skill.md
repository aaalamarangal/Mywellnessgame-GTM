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

## Three tabs per sheet

| Tab | Stands for | Who fills it | Status |
|---|---|---|---|
| Rev-B | Reviewing | The person | Active — read in every REVIEW session |
| Rem-B | Remembering | The person | Active — read in every REVIEW session |
| Rec-B | Recognising | Claude (coaching output) | Built through coaching — not an input |

## How to read a sheet

Run this command from the repo root:

```bash
python skills/read_sheet.py <sheet_id> <tab_name>
```

### Read Rev-B tab (reviewing — planning game)
```bash
python skills/read_sheet.py <sheet_id> "Rev-B"
```

### Read Rem-B tab (remembering — reflection game)
```bash
python skills/read_sheet.py <sheet_id> "Rem-B"
```

---

## Rev-B Column Map (Planning Game)

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

## Rem-B Column Map (Reflection Game)

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

## First-time setup

If the libraries are not installed, run:
```bash
pip install google-auth google-auth-httplib2 google-api-python-client
```

Credentials file must be at: `credentials/google-sheets-key.json`
