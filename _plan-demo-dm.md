# Plan — Demo DM Layer
Date: March 9, 2026
Status: DRAFT — for Shiva review

---

## The gap this fills

Public commenting has a ceiling. When a conversation needs to go from universal to personal — and the personal version requires the founder to publicly admit something vulnerable — the public thread stops working.

Demo DM is the bridge between public commenting and demo call.

---

## Founder qualification thresholds

These rules apply across all demo messaging — commenting and DM combined.

| Rule | Threshold |
|---|---|
| Messages sent (min) | 6 — don't stop early if signal is still active |
| Messages sent (max) | 9 — hard stop. No more messages after 9. |
| Replies needed to continue | 3 — if you haven't received 3 replies by the time you hit the max, stop messaging. |
| Below 3 replies at max | Stop. This founder is not ready. No more messages. |

**Why this works:**
- 6 minimum stops premature giving up after one silence
- 9 maximum stops over-investing in founders who aren't converting
- 3 replies is the signal that real conversation is happening — below that, the gap isn't live enough yet

**What to do when you stop:**
- Log the final entry in demo-message-log.md — mark as CLOSED (no fit signal)
- Move to /_archive in demo-message-log.md (or mark clearly as inactive)
- Don't delete. Signal may reactivate later.

---

## Current founder status against thresholds

| Founder | Messages sent | Replies received | Status |
|---|---|---|---|
| Rana Naskar | 3 | 2 | Active — continue |
| Leta Lista | 1 | 2 | Active — strong signal |
| Jordan Peace | 2 | 0 | Active — monitor |
| Tim Scheuer | 1 | 0 | Active — monitor |
| Manaal Maniyar | 1 | 0 | Active — monitor |
| Ross Geiger | 2 | 0 | Active — monitor |
| Nick Ang | 2 | 0 | Active — HOLDING |
| Stephen Whitworth | 1 | 0 | Active — monitor |
| Christina Qi | 1 | 0 | Active — monitor |
| Thenuka Karunaratne | 2 | 0 | Active — monitor |

No founder is near the max yet. But the pattern is visible — only Rana and Leta have replies.

---

## Where it fits in the framework

Current Value Creation OS:
1. Finding demand — signal reading, sourcing, angle
2. Capturing demand — demo-message-log (T1–T4)
3. Fulfilling demand — demo commenting (3 jobs: gap named, use case connected, fit question asked)

Demo DM is **not a new layer.** It is a channel decision within fulfilling demand.

Same 3 jobs. Same tollgates. Different channel — private instead of public.

```
Fulfilling demand
  └── Demo commenting (public)
  └── Demo DM (private — when public thread hits a ceiling)
```

---

## When to shift from comment to DM

Three conditions. All three should be true before sending a DM.

| Condition | What it means |
|---|---|
| Minimum three replies from the founder | Three replies across public threads — comments, reactions, replies on your post. DM is a continuation, not cold outreach. Below three, stay in public. |
| Public thread has a ceiling | Going personal would require the founder to publicly admit something that makes them look bad — failure, blind spot, leadership gap. |
| Signal is still active | The gap is still live for them. Not a resolved or celebration state. |

If any of these is missing — stay in the public thread or wait for a new signal.

**Why three replies:**
One reply = curiosity. Two replies = interest. Three replies = the founder is in a real conversation. At three, a DM feels like a natural continuation. Below three, it feels like a shortcut.

---

## How to write the DM opening

The DM must do one thing: make the shift from public to private feel natural, not intrusive.

**Formula:**
1. Reference the public exchange — name the specific moment or thread
2. One sentence that names what couldn't be said in public
3. One question — same as a comment, but goes to the personal layer

**What makes it intrusive:**
- No reference to prior exchange (feels cold)
- Introduces your offer or framework
- Asks for a call
- More than 100 words

**What makes it natural:**
- Opens with something they already said
- Makes clear why you moved to DM (the public thread couldn't hold the question)
- One question only — same filter rule as commenting

---

## Draft DM for Rana Naskar

**Prior exchange:** Rana described ownership drift signals universally. Asked in public: "Did you notice them, or only in hindsight?" — no reply. The personal version (admitting he missed the signals on someone he fired) is too vulnerable for a public thread.

**Draft DM:**
> "Rana — I moved this to DM because the question I wanted to ask was too personal for the thread. You described the signals well — enthusiasm fades, feedback thins, ideas stop. With the person last month: did you actually see them in time, or did they only become clear at the firing?"

Word count: 56 words. One question. References the public exchange. Names why it moved to DM. No pitch.

---

## What to add to the repo

**1. New context doc**
Path: `3.Recognising fulfilling demand/1.context/demo-dm.md`
Content: When to DM, DM formula, what makes it natural vs intrusive

**2. No new log needed**
demo-message-log.md already tracks DMs (Ross Geiger Interaction 1 was a DM).
DM entries go in the same log — sourcing method and where posted fields capture the channel.

**3. Update 3.Recognising fulfilling demand/CLAUDE.md**
Add demo DM as a parallel track alongside demo commenting.

**4. Update repo structure map in root CLAUDE.md**
Add demo-dm.md under 3.Recognising fulfilling demand/1.context/

**5. Add new session tag**
`> DM: [founder name]` — pull existing signal from log, draft DM opening, follow same Signal → Bridge → Voice pipeline

---

## What stays the same

- Same 3 jobs (gap named, use case connected, fit question asked)
- Same tollgates (T1–T4)
- Same 100-word rule
- Same one-question rule
- Same demo-message-log.md for logging

The only thing that changes is the channel and the opening line formula.

---

## Decision for Shiva

1. Does the "three conditions" rule for shifting to DM feel right?
2. Does the draft DM to Rana land?
3. Confirm before building the context doc and updating the repo structure.
