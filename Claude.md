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

## Three Operating Systems

### Value Creation OS
**What it is:** Understanding demand — who the founders are, what they are experiencing, and what signals they send.
**Core question:** What is breaking for this founder right now?
**Output:** Daily messages that create replies, not sales.

### Offer Creation OS
**What it is:** Understanding supply — how I package, position, and deliver the coaching.
**Core question:** What do I offer and how do I explain it?
**Output:** Messaging framework, product offer, and demo posting.

### Value Delivery OS
**What it is:** Delivering the coaching live — starting at the gap the founder already named.
**Core question:** Can the founder feel regulation in real time?
**Output:** Demo call that closes when regulation is felt.

> **Current focus:** Value Creation OS. Offer Creation OS and Value Delivery OS are being built in parallel as insights emerge.

---

## Core Rules

1. **Update before create.** Always search existing docs before making new ones. If a relevant doc exists, update it. Only create a new file if no existing doc covers the purpose.
2. **Link to parent.** Every new doc must reference the framework doc it belongs to.
3. **Archive don't delete.** Move completed entries to `/_archive` in the same folder. Never delete docs.
4. **Reference existing files.** Link to related docs wherever possible. More connections = better context.
5. **When completing a task.** Update the living doc it feeds, then move the task file to `/_archive`.
6. **One message per day.** `demo-message-log.md` gets one entry every time a message is sent. Non-negotiable.
7. **When adding a new folder or file.** Update the repo structure map in CLAUDE.md first. Map and reality must always match.
8. **When a demand signal illuminates a game.** Extract the exact founder quote from demo-message-log.md and add it to debt-signal-psychology.md under the relevant game (Clarity / Action / Lesson). Never paraphrase — exact words only.
9. **Every claude.md is a context file.** When creating or updating files in a folder, update that folder's claude.md to reflect what the folder contains and how it connects to the system. Empty claude.md files are not allowed.
10. **Write simply.** Always use simple, clear English. No complex words. No long sentences.

---

## Repo Structure

```
/ (root)
  CLAUDE.md                          ← you are here

  /1.Value creation- recognising demand/
    1.Recognising finding demand/

      1.context/
        /Debt-contexts
          founder-types.md           ← Founder A (complete), B and C (to be built)
          business-types.md          ← Business A / B / C — stage, symptoms, needs
          situation-types.md         ← 27 situations (3 founder types × 3 business types × 3 games)
          debt-signal-psychology.md  ← psychological texture of each game (Clarity / Action / Lesson)
          coaching-diagnostic.md     ← 6-layer diagnostic for finding where the founder is stuck
        /message-contexts
          signal-sources.md          ← WHERE to find founders — 6 ranked sourcing methods (grows via > FINDING)
          signal-reading.md          ← HOW to read signals — honesty levels, blocked vs coping, how to scan
          signal-angle.md            ← what angle to take — one entry per influencer (grows via > ANGLE)
          signal-comment.md          ← how to express the angle — Signal → Bridge → Voice (used in > COMMENT)
          inertia-types.md           ← 4 mental models founders use to justify doing nothing

    2.Recognising capturing demand/

      1.context/
        demand-tollgates.md          ← tollgate framework: what to sense at each checkpoint

      2.content/
        demo-message-log.md          ← master log: one entry per founder per message (signal, analysis, message, tollgates)

    3.Recognising fulfilling demand/  ← demo commenting (Value Creation OS fulfilling layer)

      1.context/
        demo-commenting.md           ← how demo commenting works (3 jobs, filter rule)

      2.content/
        (entries added as demo conversations develop)

      3.formula/
        (patterns built from demo conversations)

  /2.Offer creation- Recognising supply/
    1.Recognising finding supply/

      1.context/
        Post-principles.md           ← how founders talk about their systems publicly
        offer-positioning.md         ← competition map, three capabilities, differentiation
        product-messaging.md         ← Problem/Solution Value Proposition framework

      2.content/
        posts-log.md                 ← every post Shiva has published
        post-inspiration.md          ← raw material that feeds posts

    2.Recognising capturing supply/

      1.context/
        credit-framework.md          ← Credits as opposite of Debt — Clarity/Action/Lesson credits

      2.content/
        (entries to be built as offer is validated through founder interactions)

      3.formula/
        (patterns to be built once Content entries show repeatable structure)

    3.Recognising fulfilling supply/  ← demo posting (Offer Creation OS fulfilling layer)

      1.context/
        demo-posting.md              ← what demo posting is, principles

      2.content/
        demo-posts-log.md            ← one entry per demo post

      3.formula/
        (patterns to be built)

  /3.Value delivery- remembering demand/  ← demo call (new top-level OS)

    1.Remembering finding demand/

      1.context/
        demo-call.md                 ← how the demo call runs (starts at named gap, Macro → Micro → Nano live)

      2.content/
        (entries to be built)

      3.formula/
        (patterns to be built)

    2.Remembering capturing demand/

      1.context/
        demo-call-tollgates.md       ← what to sense during and after the call

      2.content/
        demo-call-log.md             ← one entry per demo call

      3.formula/
        (patterns to be built)

    3.Remembering fulfilling demand/

      1.context/
        (to be built)

      2.content/
        (to be built)

      3.formula/
        (to be built)

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
   → /Finding/Messaging-contexts/signal-comment.md

3. Claude outputs full analysis:
   - Game (Clarity / Action / Lesson)
   - Message angle: inertia type + where job breaks + pre-intent symptoms
   - Context: founder type, business type, situation, coping or blocked

4. Shiva reacts to the analysis — corrects if wrong
   Every correction builds the framework

5. Message finalised and sent by Shiva

6. Log in demo-message-log.md — T1 immediately after sending
   → /Capturing/demo-message-log.md

7. T2 check at 48 hours — surface from demo-message-log.md

8. T3 when reply comes

9. Pattern emerges
   → /Fulfilling/ folder
   → /Offer-creation/Remembering-supply/Context/credit-framework.md — which credit is building?

9b. Demo messaging begins (when a founder has replied and the pattern points toward fit)
   → Three jobs to complete before scheduling the demo call:
     Job 1: Founder names their own gap — not curiosity, a specific gap
     Job 2: Founder ties the gap to their current situation — specific use case, not generic
     Job 3: Founder asks a fit question — tone shifts from "is this relevant?" to "how would this work?"
   → Track in demo-message-log.md: Job 1 done? / Use case / Fit question asked
   → Do not schedule the demo call until all three are complete
   → Demo messaging is always a filter. Never switch to explaining the offer.

10. Demo call requested by founder
    → Starts at the gap the founder already named — not at an explanation of the offer
    → Run Macro → Micro → Nano template live on their real situation
    → The close happens when regulation is felt in real time

---

## Session Opening Tags

Type one tag at the start of every task.
Claude reads the folder it points to and runs the workflow defined there.

| Tag | What it does | Workflow lives in |
|---|---|---|
| `> COMMENT` | Analyze founder post, draft comment or DM | `2.Recognising capturing demand/CLAUDE.md` |
| `> FOLLOW-UP` | Continue existing founder conversation | `3.Recognising fulfilling demand/CLAUDE.md` |
| `> FINDING: [name]` | Post-finding lesson from influencer | `message-contexts/CLAUDE.md` |
| `> ANGLE: [name]` | Messaging angle lesson from influencer | `message-contexts/CLAUDE.md` |
| `> POST` | Write a GTM post | `3.Recognising fulfilling supply/CLAUDE.md` |
| `> T2` | Check 48h follow-ups | `2.Recognising capturing demand/CLAUDE.md` |
| `> LOG` | Confirm message sent, run T1 | `2.Recognising capturing demand/CLAUDE.md` |

Adding a new tag: update the relevant folder's CLAUDE.md + add one line to this table.

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
5. **Never let me skip the tollgates** — after every message sent, immediately walk Shiva through demand-tollgates.md before moving on. Use the senses framing: "Did you lead with what you sensed?" not "Did you lead with their feeling?" Then confirm T1 is logged in demo-message-log.md before closing the conversation.
6. **At the start of every session** — check demo-message-log.md for any messages older than 48 hours without Tollgate 2 logged. Surface them immediately.
7. **When Shiva shares a founder signal** — immediately run the full analysis and write it as a DRAFT entry to demo-message-log.md before any chat response. The draft entry must include: Game, Inertia type, Where job breaks, Pre-intent symptoms, Founder type, Business type, Coping or Blocked, and Draft message. Mark it clearly as [DRAFT — not sent]. Shiva reviews the file, reacts in chat, and confirms before the entry is finalised.
8. **Write to the plan file before responding** — whenever Shiva shares any query in plan mode, or asks for a template, system, post draft, or structural proposal, immediately write the full analysis or content to the plan file first. Then respond in chat with a short summary. Shiva opens the pinned tab to review. Never make Shiva ask for the file separately.
9. **At the start of every plan mode session** — remind Shiva to open and pin the current plan file in their IDE. The plan file path is shown in the plan mode system prompt at the start of each session. Every plan Claude writes goes there. Keep it open as a permanent tab.
10. **Before writing any post** — remind Shiva to check the comments section of the inspiration post or founder signal. Comments reveal what resonates, what questions people have, and sharpen the post angle before writing.