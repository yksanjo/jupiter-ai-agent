# 🤝 Jupiter AI Agent — Collaborator Onboarding

> **Welcome to the team!** This doc has everything you need to start contributing immediately.
> **Project:** Jupiter AI Trading Agent v2.0
> **GitHub:** https://github.com/yksanjo/jupiter-ai-agent
> **Colosseum:** https://arena.colosseum.org/projects/explore/jupiter-ai-trading-agent

---

## 🎯 What This Is

An **autonomous AI agent** that monitors Solana DeFi markets and executes trades via Jupiter's APIs. It's built for hackathons and bounties — currently competing for **$100K+** across multiple events.

**What it does:**
- 📊 Monitors real-time Solana token prices via Jupiter Price API v3
- 🔍 Searches and discovers tokens
- 🔄 Generates optimal swap quotes via Jupiter Swap v2 Order API
- 💰 Checks lending rates
- 📈 Detects arbitrage opportunities (direct vs via-SOL paths)
- 🤖 Runs continuous autonomous diagnostics
- 📝 Generates detailed Developer Experience (DX) feedback reports

**Why it's novel:**
- Not another trading bot — it's an **AI agent framework** demonstrating autonomous API discovery
- Uses `llms.txt` for LLM-optimized documentation consumption
- Self-tests all available endpoints and reports structured feedback
- Operates continuously with state persistence across restarts

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| **Language** | Python 3.8+ |
| **HTTP** | `aiohttp` (async) |
| **State** | JSON file persistence |
| **APIs** | Jupiter Price v3, Swap v2 Order/Build, Lend, Tokens |
| **SSL** | Custom context (macOS compatible) |
| **Dependencies** | Only `aiohttp` (minimal!) |

**File count:** ~4 files, ~360 lines of Python
**Complexity:** Low — designed for rapid iteration and hackathon speed

---

## 🚀 Quick Start (5 Minutes)

```bash
# 1. Clone the repo
git clone https://github.com/yksanjo/jupiter-ai-agent.git
cd jupiter-ai-agent

# 2. Install dependencies
pip install aiohttp

# 3. Set your Jupiter API key (get from https://dev.jup.ag)
export JUPITER_API_KEY="your_api_key_here"

# 4. Run the agent
python3 jupiter_ai_agent.py
```

**Expected output:**
```
🧪 Jupiter API Full Diagnostic Suite v2.0
===========================================

[1/5] Testing Price API...
       Result: ✅ Success
[2/5] Testing Multi-Price API...
       Result: ✅ Success
[3/5] Testing Swap v2 Quote API...
       Result: ✅ Success
[4/5] Testing Swap v2 Order API...
       Result: ✅ Success
[5/5] Testing Arbitrage Detection...
       Result: ✅ Success
```

---

## 📂 Project Structure

```
jupiter-ai-agent/
├── jupiter_ai_agent.py      # Main agent code (~360 lines)
├── agent_state.json         # Persistent state (auto-generated)
├── DX-REPORT.md             # Developer experience feedback report
├── README.md                # Project documentation
├── SUBMISSION-GUIDE.md      # Hackathon submission strategy
└── package.json             # Node.js metadata (for Superteam compatibility)
```

### `jupiter_ai_agent.py` — Key Methods

| Method | Purpose | Status |
|---|---|---|
| `get_token_price()` | Fetch single token price via Price API v3 | ✅ Working |
| `get_multiple_prices()` | Batch fetch prices for multiple tokens | ✅ Working |
| `search_tokens()` | Search tokens via Token API | ⚠️ API deprecated |
| `get_swap_quote()` | Get swap quote via Swap v2 Order API | ✅ Working |
| `get_swap_order()` | Get full swap order via Swap v2 Order API | ✅ Working |
| `get_lend_rates()` | Get lending rates via Lend API | ⚠️ API restructured |
| `find_arbitrage_opportunity()` | Detect arbitrage between paths | ✅ Working |
| `monitor_tokens()` | Continuous token monitoring loop | ✅ Working |
| `run_full_diagnostics()` | Test all APIs + generate report | ✅ Working |

---

## 🏆 Current Hackathon Submissions

| Hackathon | Prize Pool | Status | Deadline |
|---|---|---|---|
| **AI Trading Agents (Surge/Lablab)** | **$55,000** | ✅ Submitted | April 12 |
| **Frontier Hackathon (Superteam)** | **$3,000 jupUSD** | ✅ Submitted | May 12 |
| **Stellar Hacks: Agents** | **$10,000 XLM** | ⚠️ Need to submit | **April 13** |
| **Four.Meme AI Sprint** | **$50,000** | ⚠️ Need to submit | April 30 |
| **ETHGlobal Open Agents** | **$50,000+** | ⚠️ Need to submit | April 24 |

---

## 🎯 Immediate Priorities (Next 7 Days)

### 🔴 Urgent — Do This Week

1. **Stellar Hacks: Agents** (Deadline: April 13)
   - **Prize:** $10,000 in XLM
   - **Platform:** DoraHacks
   - **What to build:** AI agent that integrates with Stellar's Soroban network
   - **Action:** Fork agent, add Stellar endpoint, submit via DoraHacks
   - **Link:** https://dorahacks.io/hackathon/stellar-agents-x402-stripe-mpp

2. **Demo Video / Loom Recording** (Needed for all hackathons)
   - **Length:** 3-5 minutes
   - **Content:** Show repo → run agent → show all 5/5 APIs passing → show DX report
   - **Script:**
     ```
     1. Show GitHub repo
     2. Run: python3 jupiter_ai_agent.py
     3. Show output with all ✅ Success
     4. Show DX-REPORT.md with bug findings
     5. Explain: "This agent autonomously monitors Solana DeFi..."
     ```

3. **ETHGlobal Open Agents** (Deadline: April 24)
   - **Prize:** $50,000+
   - **Platform:** ETHGlobal
   - **What to build:** AI agent applications on Ethereum
   - **Action:** Adapt agent for Ethereum APIs (Etherscan, Uniswap)
   - **Link:** https://ethglobal.com/events/openagents

### 🟡 This Month

4. **Four.Meme AI Sprint** (Deadline: April 30)
   - **Prize:** $50,000
   - **Platform:** DoraHacks
   - **What to build:** AI × Web3 applications on BNB Chain
   - **Action:** Port agent to BNB Chain + PancakeSwap APIs
   - **Link:** https://dorahacks.io/hackathon/fourmemeaisprint

---

## 🚀 Feature Backlog (What to Build Next)

### High Priority
- [ ] **WebSocket Price Feeds** — Replace polling with real-time streams
- [ ] **Telegram/Discord Alerts** — Notify on price changes or arbitrage opportunities
- [ ] **Backtesting Engine** — Test strategies against historical data
- [ ] **Multi-Chain Support** — Add Ethereum, BNB Chain, Stellar endpoints
- [ ] **Python SDK** — `pip install jupiter-agent` with type hints
- [ ] **Docker Support** — `docker run jupiter-agent` for easy deployment

### Medium Priority
- [ ] **LangChain Integration** — Make agent usable as a LangChain tool
- [ ] **AutoGPT Plugin** — Enable agent as a plugin for autonomous agents
- [ ] **Analytics Dashboard** — Show API usage, most-called endpoints
- [ ] **Testnet/Sandbox Mode** — Test without real transactions
- [ ] **Rate Limit Tracking** — Monitor quota usage per API key
- [ ] **Error Code Reference** — Machine-parseable error responses

### Low Priority
- [ ] **Community Examples Repo** — "10 things people built"
- [ ] **Interactive API Playground** — Try endpoints in browser
- [ ] **WebSocket Price Feeds** — Instead of polling

---

## 🔑 API Keys & Credentials

| Service | URL | Status |
|---|---|---|
| **Jupiter Developer Platform** | https://dev.jup.ag | ✅ Active (Price v3, Swap v2) |
| **Superteam Earn** | https://earn.superteam.fun | ✅ Agent registered |
| **Colosseum** | https://arena.colosseum.org | ✅ Project submitted |
| **Surge/Lablab** | https://early.surge.xyz | ✅ Project created |
| **DoraHacks** | https://dorahacks.io | ⚠️ Need account |
| **ETHGlobal** | https://ethglobal.com | ⚠️ Need account |

---

## 📝 How to Contribute

1. **Fork the repo** → `https://github.com/yksanjo/jupiter-ai-agent`
2. **Create a branch** → `git checkout -b feature/my-feature`
3. **Make changes** → Keep code clean, minimal, documented
4. **Test locally** → `python3 jupiter_ai_agent.py`
5. **Commit** → `git commit -m "feat: add my feature"`
6. **Push** → `git push origin feature/my-feature`
7. **Open a PR** → Describe what you changed and why

**Code Style:**
- Keep it simple — this is a hackathon project, not production software
- Use type hints where helpful
- Document new methods with docstrings
- Test all API calls before committing

---

## 🐛 Known Issues

| Issue | Severity | Status |
|---|---|---|
| Token Search API deprecated | Medium | ⚠️ Workaround needed |
| Lend API restructured | Medium | ⚠️ Workaround needed |
| No rate limit headers from Jupiter | Low | 📝 Documented in DX report |
| Inconsistent error response formats | Low | 📝 Documented in DX report |
| macOS SSL certificate issues | Low | ✅ Fixed with custom SSL context |

---

## 💰 Bounty Hunting Strategy

We're using a **multi-platform approach** to maximize earnings:

1. **Hackathons** — Big prizes ($3K-$55K), longer timelines
2. **Superteam Earn** — Medium bounties ($500-$3K), agent-automated
3. **Proxies.sx** — Small bounties ($50-$200), GitHub PR submissions
4. **Immunefi** — Huge bounties ($10K-$3M), security research
5. **Bountycaster** — Micro bounties ($20-$5K), Farcaster-based

**Auto-monitoring:**
- `bounty-hunter-master.py` runs 24/7 checking for new bounties
- Checks Superteam, Proxies.sx, Immunefi, Code4rena every 120s
- Logs to `/tmp/bounty-hunter-master.log`

---

## 📞 Communication

- **GitHub:** All code and PRs here
- **Colosseum:** Hackathon submissions
- **Surge:** AI Trading Agents hackathon
- **DoraHacks:** Multiple hackathon tracks

**When you're ready to start:**
1. Clone the repo
2. Run the agent to see it working
3. Pick a priority from the backlog
4. Start coding!

---

*This document is a living doc — update it as the project evolves.*
*Last updated: April 12, 2026*
