# Copia AI MCP: LinkedIn Live Scraping for Value Creation OS
Parent: CLAUDE.md | Weekly | Infrastructure setup

## Status: Ready to execute — waiting on MCP credentials from Copia AI dashboard

---

## Context

Manual copy-paste of LinkedIn post content into Claude is real friction in the Value Creation OS. Tim Scheuer's Copia AI provides a live MCP server with 40+ GTM integrations including direct LinkedIn access.

**Why this doesn't violate the "no automation" rule:**
- Shiva still chooses who to look at — no automated targeting
- Claude fetches the content, Shiva reads the analysis
- Shiva still approves the DRAFT before any message is sent
- Shiva still sends manually
- All tollgates still run

MCP = research fetch. The judgment layer never moves to Claude.

---

## Phase 1 — Copia AI Setup

### Step 1: Sign up ← DONE
- Code: **LAUNCH** (30% off)
- URL: **https://copia-ai.com/**
- Tim confirmed: live scraping via third-party provider ✅
- Use case confirmed: fetch context for messaging, not cold DMs ✅

### Step 2: Connect MCP to Claude Code
1. Log into Copia AI dashboard
2. Find the MCP server URL + API key
3. Add to `C:\Users\LENOVO\.claude\settings.json`:

```json
{
  "autoMemoryEnabled": true,
  "mcpServers": {
    "google-drive": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-gdrive"]
    },
    "copia": {
      "type": "sse",
      "url": "<MCP server URL from Copia AI dashboard>",
      "headers": {
        "Authorization": "Bearer <your API key>"
      }
    }
  }
}
```

4. Restart Claude Code so the new MCP server loads.

### Step 3: Critical test before updating workflow docs

**Tim said:** "you can fetch the leads LinkedIn profile + posts"

**Verify this before updating docs:**
> Can the LinkedIn integration also fetch a founder's comment activity — their replies on other people's posts and their replies to comments on their own posts?

Signal honesty ranking (from linkedin-signal-scraping.md):
- Replies on other people's posts ← most honest
- Replies to their own post comments ← candid
- Their own posts ← most performative

**Test:** Give Claude a known founder's LinkedIn URL. Ask for posts AND comment activity. See what comes back.

If comments included → full workflow update
If posts only → still useful, comment/reply layer stays manual

### Step 4: Update workflow docs (after test confirms what's available)

**File 1: `linkedin-signal-scraping.md`** — add MCP-Assisted Scan section at top
**File 2: `CLAUDE.md`** — update Thinking Path Step 1
**File 3: message-contexts/claude.md** — update folder context

---

## Phase 2 — Evaluate Other MCP Providers (after Copia AI trial)

| Provider | LinkedIn post+comments? | MCP? |
|---|---|---|
| PhantomBuster | Yes | Check |
| Apify | Yes | Yes |
| Apollo | Contact data only | Unknown |
| Prospeo | Email finder only | Unknown |

Evaluate after Copia AI trial — only switch if comment/reply fetching is missing or cost is prohibitive.

---

## When This Is Done

The Thinking Path Step 1 becomes:
> "Shiva shares: founder LinkedIn profile URL → Claude fetches posts, comments, and replies via MCP"

Instead of:
> "Shiva shares: founder link + post link + post content"

Everything from Step 2 onward (signal analysis, DRAFT entry, message, tollgates) stays identical.
