# CLAUDE.md — mywellnessgame Operating System

This is the context system for running mywellnessgame — a productivity coaching business
helping founders build sustainable productivity systems.

Open Code has full access. Follow these rules strictly.

---

## What This Business Does

Shiva Kumar coaches founders to build persistent productivity systems using a 3-Game Framework.
The methodology: Being + Doing = Having.
The daily non-negotiable: Send ONE message to ONE founder. Every day. No exceptions.

**Debt / Credit polarity:**
- Clarity → Clarity Credit → To do → Speed
- Action  → Action Credit  → Assessment → Leverage
- Lesson  → Lesson Credit  → Journal → Multiplier

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

> **Current focus:** Value Creation OS. Offer Creation OS is being built in parallel as insights emerge.

---

## Core Rules

1. **Update before create.** Always search existing docs before making new ones. If a relevant doc exists, update it. Only create a new file if no existing doc covers the purpose.
2. **Link to parent.** Every new doc must reference the framework doc it belongs to.
3. **Archive don't delete.** Move completed entries to `/_archive` in the same folder. Never delete docs.
4. **Reference existing files.** Link to related docs wherever possible. More connections = better context.
5. **When completing a task.** Update the living doc it feeds, then move the task file to `/_archive`.
6. **One message per day.** `prospect-log.md` gets one entry every time a message is sent. Non-negotiable.
7. **When adding a new folder or file.** Update the repo structure map in CLAUDE.md first. Map and reality must always match.
8. **When a demand signal illuminates a game.** Extract the exact founder quote from prospect-log.md and add it to debt-signal-psychology.md under the relevant game (Clarity / Action / Lesson). Never paraphrase — exact words only.
9. **Every claude.md is a context file.** When creating or updating files in a folder, update that folder's claude.md to reflect what the folder contains and how it connects to the system. Empty claude.md files are not allowed.
10. **Write simply.** Always use simple, clear English. No complex words. No long sentences.

---

## Repo Structure

```
/ (root)
  CLAUDE.md                          ← you are here

  /Value-creation
    /Recognising-demand

      /Finding (context layer — understanding who the founder is)
        /Debt-contexts
          founder-types.md           ← Founder A (complete), B and C (to be built)
          business-types.md          ← Business A / B / C — stage, symptoms, needs
          situation-types.md         ← 27 situations (3 founder types × 3 business types × 3 games)
          debt-signal-psychology.md  ← psychological texture of each game (Clarity / Action / Lesson)
          coaching-diagnostic.md     ← 6-layer diagnostic for finding where the founder is stuck
        /Messaging-contexts
          sources.md                 ← lessons from coaches, mentors, influencers
          signal-bridge-voice.md     ← translation pipeline: Signal → Bridge → Voice
          inertia-types.md           ← 4 mental models founders use to justify doing nothing

      /Capturing (content layer — sending messages, logging interactions)
        prospect-log.md              ← master log: one entry per founder per message (signal, analysis, message, tollgates)
        linkedin-signal-scraping.md  ← how to find signals on LinkedIn (3 sources)
        demand-tollgates.md          ← tollgate framework: what to sense at each checkpoint

      /Fulfilling (formula layer — repeatable patterns, to be built over time)

  /Offer-creation
    /Recognising-supply
      /Context
        claude.md                    ← folder context file
        Post-principles.md           ← how founders talk about their systems publicly — informs future posting voice
        offer-positioning.md         ← competition map, three capabilities, differentiation, positioning draft
        product-messaging.md         ← Problem/Solution Value Proposition framework for mywellnessgame

      /Content
        (to be built — product messaging, demo call structure)

      /Formula
        (to be built — repeatable offer delivery)

    /Remembering-supply
      /Context
        claude.md                    ← folder context file
        credit-framework.md          ← Credits as opposite of Debt — Clarity/Action/Lesson credits, solution dimensions, focus areas

      /Content
        claude.md                    ← folder context file
        (entries to be built as offer is validated through founder interactions)

      /Formula
        claude.md                    ← folder context file
        (patterns to be built once Content entries show repeatable structure)

  /Weekly
    This-Week.md                     ← current week only (replace each Friday)
    /_archive                        ← past weeks

  /Clients                           ← to be created when first paying customer arrives
```

---

## Thinking Path — From Signal to Demo Call

This is the sequence Claude must follow to support Shiva from first signal to demo call requested by a founder.

1. Shiva shares: founder link + post link + post content

2. Claude reads signal through game contexts
   → /Finding/Debt-contexts/
   → /Finding/Messaging-contexts/signal-bridge-voice.md

3. Claude outputs full analysis:
   - Game (Clarity / Action / Lesson)
   - Message angle: inertia type + where job breaks + pre-intent symptoms
   - Context: founder type, business type, situation, coping or blocked

4. Shiva reacts to the analysis — corrects if wrong
   Every correction builds the framework

5. Message finalised and sent by Shiva

6. Log in prospect-log.md — T1 immediately after sending
   → /Capturing/prospect-log.md

7. T2 check at 48 hours — surface from prospect-log.md

8. T3 when reply comes

9. Pattern emerges
   → /Fulfilling/ folder
   → /Offer-creation/Remembering-supply/Context/credit-framework.md — which credit is building?

10. Demo call requested by founder

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
5. **Never let me skip the tollgates** — after every message sent, walk me through demand-tollgates.md before moving on. Use the senses framing: "Did you lead with what you sensed?" not "Did you lead with their feeling?"
6. **After every message sent** — remind Shiva to log Tollgate 1 immediately before closing the conversation
7. **At the start of every session** — check prospect-log.md for any messages older than 48 hours without Tollgate 2 logged. Surface them immediately.
8. **Every Wednesday** — ask Shiva: "What's one way I could coach you better this week?" Update this section based on the answer.
9. **When Shiva shares a founder signal** — immediately run the full analysis and write it as a DRAFT entry to prospect-log.md before any chat response. The draft entry must include: Game, Inertia type, Where job breaks, Pre-intent symptoms, Founder type, Business type, Coping or Blocked, and Draft message. Mark it clearly as [DRAFT — not sent]. Shiva reviews the file, reacts in chat, and confirms before the entry is finalised.
10. **In plan mode, write before you respond** — whenever Shiva shares any query or request while in plan mode, immediately write the full analysis, proposal, or breakdown to the plan file first. Then respond in chat with a short summary. Shiva opens the file to review the detail. Never make Shiva ask for the file separately.