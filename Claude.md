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

## Core Rules

1. **Update before create.** Always search existing docs before making new ones. If a relevant doc exists, update it. Only create a new file if no existing doc covers the purpose.
2. **Link to parent.** Every new doc must reference the framework doc it belongs to.
3. **Archive don't delete.** Move completed entries to `/_archive` in the same folder. Never delete docs.
4. **Reference existing files.** Link to related docs wherever possible. More connections = better context.
5. **When completing a task.** Update the living doc it feeds, then move the task file to `/_archive`.
6. **One message per day.** `daily-message-log.md` gets one entry every day before end of day. Non-negotiable.
7. **When adding a new folder or file.** Update the repo structure map in CLAUDE.md first. Map and reality must always match.
8. **When a demand signal illuminates debt psychology.** Extract the exact founder quote from demand-signals.md and add it to debt-psychology.md under the relevant debt stage (Context / Content / Formula). Never paraphrase — exact words only.

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
        demand-signals.md            ← raw signals from founders (currently LinkedIn)
        demand-translation.md        ← converting signal into message
        sent-messages.md             ← actual messages sent

      /Formula
        (empty — patterns to be built over time)

    /Remembering-demand
      /Context
        demand-tollgates.md          ← checkpoints that frame what happens after sending

      /Content
        daily-message-log.md         ← one entry per day, what happened at each tollgate

      /Formula
        (empty — patterns to be built over time)

  /Weekly
    This-Week.md                     ← current week only (replace each Friday)
    /_archive                        ← past weeks

  /Clients                           ← to be created when first paying customer arrives
```

---

## Thinking Path — From Signal to Demo Call

This is the sequence Claude must follow to support Shiva from first signal to demo call requested by a founder.

1. Recognise the signal
   → /Recognising-demand/Content/demand-signals.md

2. Identify debt stage
   → /Recognising-demand/Context/Debt-contexts/
   → /Recognising-demand/Context/Messaging-contexts/debt-psychology.md

3. Translate into message
   → /Recognising-demand/Content/demand-translation.md

4. Send the message
   → /Recognising-demand/Content/sent-messages.md

5. Position at tollgates — observe founder response
   → /Remembering-demand/Context/demand-tollgates.md
   → /Remembering-demand/Content/daily-message-log.md

6. Pattern emerges
   → /Recognising-demand/Formula/
   → /Remembering-demand/Formula/

7. Demo call requested by founder

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
5. **Never let me skip the tollgates** — after every message sent, walk me through demand-tollgates.md before moving on
6. **Every Wednesday** — ask Shiva: "What's one way I could coach you better this week?" Update this section based on the answer.