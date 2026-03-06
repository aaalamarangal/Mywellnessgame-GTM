# Anusya MCP Brief — Build the First Callable Skill

## What you are building and why

Shiva coaches founders using a Macro → Micro → Nano framework.
The first validated skill: a tool that maps any founder situation to this structure.

Sujith (paying client) used it and said: "the experience of doing this is wild" and "it is building courage."

The goal today: make this skill callable from a founder's Claude Code terminal.

---

## The stack

```
CLI   = founder's Claude Code terminal (where they type)
MCP   = connector that exposes the skill as a callable tool
Skill = the judgment (Macro → Micro → Nano diagnosis)
API   = mechanical layer underneath (not needed at MVP)
```

---

## Step 1 — Read the skill definition

File: `C:\Mywellnessgame-GTM-main\2.Offer creation- Recognising supply\CLAUDE.md`

Read the "First Validated Skill" section.
This contains:
- The 11 template columns with exact questions
- Sujith's worked example (the training material for your prompt)
- What the skill can and cannot do

This is your input/output spec. Understand it before building.

---

## Step 2 — Set up a basic MCP server

Use Python (FastMCP) or Node.js (MCP SDK). One file is enough.

MCP SDK docs: https://modelcontextprotocol.io/quickstart/server

---

## Step 3 — Define one tool: `map_game`

**Input:**
```
situation: string  ← the founder describes what they are working on today
```

**Output (structured):**
```
macro_game: string            ← high-leverage outcome (6–12 weeks)
micro_game: string            ← stepping stone to macro (1–6 weeks)
nano_game: string             ← what to do today (1–3 weeks)
constraint_game_type: string  ← Clarity / Action / Lesson
constraint_sub_credit: string ← concepts / qualities / tasks / tactics / workflows / capabilities
next_steps: string            ← what to do during the day
```

---

## Step 4 — Write the skill prompt

The tool does not call an external API. It calls Claude with a structured prompt.

The prompt must instruct Claude to:
1. Read the founder's situation
2. Map it to Macro → Micro → Nano using the 11-column structure
3. Identify the Game type at Nano level (Clarity / Action / Lesson)
4. Identify the Sub-credit constraint (which of the 6 layers is the bottleneck)
5. Generate next steps for the day

Use Sujith's worked example from CLAUDE.md as the few-shot example inside the prompt.

---

## Step 5 — Test it locally in Claude Code

1. Start the MCP server
2. Add it to Claude Code settings (`.claude/settings.json` or `~/.claude.json`)
3. Ask Claude Code: "map my game — I am trying to [founder's situation]"
4. Confirm Claude returns all 6 output fields

---

## What success looks like

A founder types their situation into Claude Code.
Claude returns a filled Macro → Micro → Nano structure.
The output matches what Shiva would fill manually.

That is the MVP. One tool. One skill. Working locally.

---

## What NOT to build today

- Database or persistence layer
- Multiple tools
- UI or front-end
- Authentication

---

## Files you need

1. `C:\Mywellnessgame-GTM-main\2.Offer creation- Recognising supply\CLAUDE.md` — skill definition and Sujith's worked example
2. MCP SDK docs: https://modelcontextprotocol.io/quickstart/server

---

## After you build

Share the MCP server file and a screenshot of the test output with Shiva.
Shiva will compare the output to what he would have filled manually.
If it matches — the skill is encoded.
