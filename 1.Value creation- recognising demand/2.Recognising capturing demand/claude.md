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
   - Layer 0 positioning orientation precedes the pipeline — see signal-comment.md for the checklist. Positioning Type flows automatically from the inertia type (see inertia-types.md mapping).
3. Write DRAFT entry to demo-message-log.md (marked [DRAFT — not sent])
4. Show full diagnosis in chat — in this order:
   a. Signal section (Game, Inertia type, pre-intent symptoms, Coping or Blocked)
   b. Bridge section (where job breaks, ICP motivator, anchor sentence)
   c. Three jobs layer — where Job 1 could land, what Job 2 looks like, what Job 3 signal to watch for
   d. Draft message last — so Shiva reads the thinking first and decides on the words himself
5. Wait for Shiva to react and confirm before finalizing
6. Post Arc check — ask: does the exact founder language belong in the Post Arc Tracker?
   Three triggers:
   - Exact words that name a gap better than Shiva could
   - Same gap named independently by two or more founders
   - A client result moment — something shifted in real time
   If yes: add a row to the Post Arc Tracker in post-inspiration.md and log exact words immediately. Same session, not later.
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
