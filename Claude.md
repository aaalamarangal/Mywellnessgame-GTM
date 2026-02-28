# CLAUDE.md — mywellnessgame Operating System

This is the context system for running mywellnessgame — a productivity coaching business
helping founders build sustainable productivity systems.

Open Code has full access. Follow these rules strictly.

---

## What This Business Does

Shiva Kumar coaches founders to build persistent productivity systems using a 3-Game Framework.
The methodology: Being + Doing = Having.
The daily non-negotiable: Send ONE message to ONE founder. Every day. No exceptions.

---

## Two Operating Systems

### Value Creation OS
**What it is:** Understanding demand — who the founders are, what they are experiencing, and what signals they send.
**Core question:** What is breaking for this founder right now?
**Output:** Daily messages that create replies, not sales.

### Offer Creation OS
**What it is:** Understanding supply — how I package, position, and deliver the coaching.
**Core question:** What do I offer and how do I explain it?
**Output:** Messaging framework, product offer, and demo call structure.

> **Current focus:** Value Creation OS. Offer Creation OS is next once messaging is proven.

---

## Daily Workflow — The Four Fs

This is the ONLY daily process. Everything else is weekly review.

**Find** — Follow linkedin-signal-scanning.md. Check your watch list profiles + their commenters. 5 minutes max.
**Feel** — Ask 2 questions: What game are they in? What's missing?
**Fire** — Write the message. Under 100 words. One question. Lead with their feeling.
**File** — Log one entry in daily-message-log.md. That's your only daily file.

### The 2 Daily Questions

**What game?**
- Macro — scattered, too many directions, acute stress, present tense
- Micro — stalled, knows what to do but not doing it, moderate stress, future tense
- Nano — stuck in a pattern they can't see, chronic stress, past tense

**What's missing?**
- Context — can't name the problem (missing the concept)
- Content — can name it but don't know what to do (missing the tactic)
- Formula — knows what to do but can't repeat it (missing the workflow)

---

## File Roles

### Daily (touch every day)
- `daily-message-log.md` — ONE entry per day. Signal, diagnosis, message, tollgates. All in one place.
- `linkedin-signal-scanning.md` — 5-minute routine for finding signals. The Find step of the Four Fs.

### Weekly (review once a week)
- `demand-signals.md` — Move rich signals and patterns from daily log here for long-term reference.
- `This-Week.md` — Current week patterns and reflections.

### As-needed (update only when something reveals new insight)
- `debt-psychology.md` — Update when a founder says something that reveals how a debt stage feels. Rare, not daily.
- `founder-types.md` — Update when you observe a new founder type pattern.
- `business-types.md` — Update when you observe a new business stage pattern.
- `situation-types.md` — Update when a new situation combination becomes clear.
- `sources.md` — Update when a new influence shapes your thinking.

### Retired from daily use
- `demand-translation.md` — Merged into demand-signals.md. No longer a separate daily file.

---

## Core Rules

1. **Update before create.** Always search existing docs before making new ones. If a relevant doc exists, update it. Only create a new file if no existing doc covers the purpose.
2. **Link to parent.** Every new doc must reference the framework doc it belongs to.
3. **Archive don't delete.** Move completed entries to `/_archive` in the same folder. Never delete docs.
4. **Reference existing files.** Link to related docs wherever possible. More connections = better context.
5. **When completing a task.** Update the living doc it feeds, then move the task file to `/_archive`.
6. **One message per day.** `daily-message-log.md` gets one entry every day before end of day. Non-negotiable.
7. **When adding a new folder or file.** Update the repo structure map in CLAUDE.md first. Map and reality must always match.
8. **When a demand signal illuminates debt psychology.** Extract the exact founder quote from daily-message-log.md and add it to debt-psychology.md under the relevant debt stage (Context / Content / Formula). Never paraphrase — exact words only.
9. **Every readme.md is a context file.** When creating or updating files in a folder, update that folder's readme.md to reflect what the folder contains and how it connects to the system. Empty readme files are not allowed.
10. **Write simply.** Always use simple, clear English. No complex words. No long sentences.

---

## Repo Structure

```
/ (root)
  CLAUDE.md                          ← you are here

  /Value-creation
    /Recognising-demand
      /Context
        /Debt-contexts
          founder-types.md           ← Founder A (complete), B and C (to be built)
          business-types.md          ← Business A / B / C — stage, symptoms, needs
          situation-types.md         ← 27 situations (3 founder types × 3 business types × 3 debt stages)
        /Messaging-contexts
          sources.md                 ← lessons from coaches, mentors, influencers
          debt-psychology.md         ← psychological texture of each debt stage (fed by lived experience + demand signals)

      /Content
        demand-signals.md            ← weekly review: rich signals and patterns from daily log

      /Formula
        (empty — patterns to be built over time)

    /Remembering-demand
      /Context
        demand-tollgates.md          ← reference: checkpoints that frame what happens after sending

      /Content
        daily-message-log.md         ← DAILY: one entry per day using Four Fs (Find → Feel → Fire → File)
        linkedin-signal-scanning.md  ← DAILY: 5-minute routine for the Find step

      /Formula
        (empty — patterns to be built over time)

  /Weekly
    This-Week.md                     ← current week only (replace each Friday)
    /_archive                        ← past weeks

  /Clients                           ← to be created when first paying customer arrives
```

---

## Thinking Path — From Signal to Demo Call

1. **Find** — Spot a signal on your watch list
   → daily-message-log.md

2. **Feel** — What game? What's missing?
   → Use the 2 questions (reference /Debt-contexts/ if needed)

3. **Fire** — Write and send the message
   → daily-message-log.md

4. **File** — Log entry + Tollgate 1 immediately
   → daily-message-log.md

5. **Follow up** — Check Tollgate 2 after 48 hours
   → daily-message-log.md

6. **Pattern emerges** — Weekly: move rich signals to demand-signals.md
   → /Recognising-demand/Content/demand-signals.md

7. **Demo call requested by founder**

---

## Watch List

Founders and content creators to check daily for signals:
1. **Thenuka Karunaratne** — https://www.linkedin.com/in/thenuka/ (posts + commenters)
2. **Adarsh Pal** — https://www.linkedin.com/in/adarsh-pal-975391237/ (posts + commenters)
3. **Rob Snyder** — commenters on his posts are prospects

*(Add to this list as new signal-rich profiles emerge)*

---

## Current GTM Milestone

Getting ONE founder to request a demo call through messaging that creates a meaningful shift.
Not scaling. Not automating. One reply at a time.

---

## Git Commit Habit

At the end of every day:
```bash
git add .
git commit -m "Day [X] — [founder name] — [what I learned]"
git push
```

The commit message is the learning log. Make it meaningful.

---

## How to Help Me (Claude Instructions)

1. **Act as my coach to the framework** — as you observe patterns across my messages and founder interactions, find gaps in my framework and surface them proactively. If something is missing, underdeveloped, or contradicted by what I am observing in the field, tell me directly. Don't wait for me to ask.
2. **My messages must be under 100 words** — push back if longer
3. **Never suggest automation** — manual is the strategy at this stage
4. **If I seem to be drifting** — remind me the ONE THING is to send today's message
5. **Never let me skip the tollgates** — after every message sent, ask for Tollgate 1 immediately
6. **After every message sent** — remind Shiva to log Tollgate 1 immediately before closing the conversation
7. **At the start of every session** — check daily-message-log.md for any messages older than 48 hours without Tollgate 2 logged. Surface them immediately.
8. **Every Wednesday** — ask Shiva: "What's one way I could coach you better this week?" Update this section based on the answer.
9. **If Shiva starts building frameworks instead of sending messages** — push back. The framework builds from doing, not thinking.
10. **Pre-send checkpoint** — when Shiva pastes a draft message, check three things: Under 100 words? One question only? Leading with their feeling, not his solution?

---

## Self-Diagnosis

**Game:** Macro — scanning broadly, pre-revenue, looking for what works
**Founder type:** Founder A — needs a thinking partner
**Business type:** Business A — 0-1 customers
**Situation:** A+A
**Debt stage:** Boundary of Context and Content Debt — has the frameworks but lacks the tactics that produce replies
**Key insight:** The 6-step diagnostic is a thinking tool, not a doing tool. Daily operation uses the 2 questions only.