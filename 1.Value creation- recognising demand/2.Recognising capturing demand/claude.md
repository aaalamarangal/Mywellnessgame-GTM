# 2.Recognising capturing demand
Parent: 1.Value creation- recognising demand | CLAUDE.md

## What this folder is

This is the capturing layer of Value Creation OS.
It tracks all demo messaging — from first contact through to demo call request.

## Sub-folders

- **1.context/** — demand-tollgates.md (what to sense at each checkpoint)
- **2.content/** — demo-message-log.md (master log: one entry per founder per message)

## How it connects

- Incoming: signals found in 1.Recognising finding demand/
- Outgoing: when all 3 jobs are complete (gap named, use case connected, fit question asked), founder moves to 3.Value delivery- remembering demand/

---

## Task Workflows

### > COMMENT
Shiva shares: founder name, post URL, exact post text, type (public comment or DM)

Claude does:
1. Read the signal through game contexts (debt-signal-psychology.md, founder-types.md, inertia-types.md)
2. Walk the writing-pipeline.md steps: Signal → Bridge → Voice
   - Signal: Game / Inertia type / Pre-intent symptoms / Founder type / Business type / Coping or Blocked
   - Bridge: Inertia type + where job breaks + pre-intent symptoms → one message anchor sentence
   - Voice: under 100 words, one question, leads with what you sensed — not the framework
3. Write DRAFT entry to demo-message-log.md (marked [DRAFT — not sent])
4. Summarize analysis in chat — short, no preamble
5. Wait for Shiva to react before finalizing
(Process follows signal-comment.md — informed by signal-angle.md in the background)

### > T2
Shiva types: > T2 — no other input needed

Claude does:
1. Open demo-message-log.md
2. Find every entry where T2 is not logged and message was sent 48h+ ago
3. Surface each one: founder name, date sent, signal summary, suggested check-in question
4. Walk Shiva through each one before moving on

### > LOG
Shiva shares: founder name, exact message/comment sent, date sent, type (DM or public comment)

Claude does:
1. Find the DRAFT entry in demo-message-log.md for this founder
2. Mark as sent — fill in exact text and date
3. Fill Tollgate 1
4. Walk Shiva through demand-tollgates.md immediately
5. Confirm T1 is logged before closing
