# 🎯 Active Bounty & Hackathon Submission Guide

**Project:** Jupiter AI Agent v2.0  
**GitHub:** https://github.com/yksanjo/jupiter-ai-agent  
**Status:** All 5/5 Jupiter APIs working, code pushed, DX report complete

---

## 🔴 URGENT — Submit Within 1-2 Days

### 1. Surge x Kraken: AI Trading Agents
- **Prize Pool:** $55,000
- **Deadline:** April 12, 2026 (TOMORROW!)
- **Platform:** lablab.ai
- **Registration:** https://lablab.ai/event/ai-trading-agents
- **Why Submit:** Our Jupiter AI Agent is literally an AI trading agent that monitors prices, gets swap quotes, and detects arbitrage on Solana
- **What to Do:**
  1. Register on lablab.ai
  2. Submit GitHub repo: https://github.com/yksanjo/jupiter-ai-agent
  3. Write project description focusing on AI agent's autonomous price monitoring, swap quote generation, and arbitrage detection
  4. Record a quick Loom demo showing the agent running (`python3 jupiter_ai_agent.py`)

### 2. Stellar Hacks: Agents
- **Prize Pool:** $10,000 in XLM
- **Deadline:** April 13, 2026 (2 DAYS!)
- **Platform:** DoraHacks
- **Theme:** AI Agents + Payments (x402 on Stellar, MPP-style flows)
- **Registration:** https://dorahacks.io/hackathon/stellar-agents-x402-stripe-mpp/hackers
- **Why Submit:** Our AI agent could be adapted to work with Stellar's Soroban network + the payment agent theme fits
- **What to Do:**
  1. Register on DoraHacks
  2. Submit as "AI Payment Agent" — adapt the Jupiter agent concept to Stellar
  3. Focus on how AI agents can autonomously check prices, execute trades, and handle payments

---

## 🟡 HIGH PRIORITY — Submit This Week

### 3. Solana Frontier Hackathon (Colosseum)
- **Grand Champion:** $30,000
- **Public Goods Award:** $10,000
- **University Award:** $10,000
- **20 Standout Teams:** $10,000 each
- **Accelerator:** $250,000 pre-seed for winners
- **Deadline:** May 11, 2026
- **Platform:** Colosseum
- **Registration:** https://colosseum.com/frontier
- **Superteam Earn Bounty:** $3,000 jupUSD (also submit via Superteam Earn)
- **Why Submit:** Our project is built specifically for this hackathon. The Jupiter DX report directly addresses their API.
- **What to Do:**
  1. Register at colosseum.com/frontier
  2. Join Colosseum Discord for workshops/office hours
  3. Submit GitHub repo + DX report
  4. Record a Loom demo (3-5 min)
  5. Also submit to Superteam Earn bounty (see below)

### 4. The Bags Hackathon
- **Deadline:** June 1, 2026
- **Platform:** DoraHacks
- **Theme:** Solana ecosystem
- **Registration:** https://dorahacks.io/hackathon/the-bags
- **Why Submit:** Pure Solana hackathon — our Jupiter agent is a perfect fit
- **What to Do:**
  1. Register on DoraHacks
  2. Submit project

---

## 🟢 MEDIUM PRIORITY — Submit This Month

### 5. Superteam Earn — "Not Your Regular Bounty" (Frontier Hackathon)
- **Reward:** $3,000 jupUSD
- **Deadline:** May 12, 2026
- **Platform:** Superteam Earn
- **Status:** Attempted submission but Colosseum profile URL validation failed
- **What to Do:**
  1. Go to https://earn.superteam.fun
  2. Find "Not Your Regular Bounty" listing
  3. Submit manually through the web UI (the API has strict URL validation)
  4. Make sure to have a valid Colosseum hackathon profile URL ready

### 6. Four.Meme AI Sprint
- **Deadline:** April 30, 2026
- **Platform:** DoraHacks
- **Theme:** BNB Chain / AI
- **Registration:** https://dorahacks.io/hackathon/four-meme-ai-sprint

### 7. iExec Vibe Coding Challenge
- **Deadline:** May 1, 2026
- **Platform:** DoraHacks
- **Theme:** Arbitrum / Vibe Coding
- **Registration:** https://dorahacks.io/hackathon/iexec-vibe-coding

---

## 📋 Submission Checklist

### For Each Hackathon, Prepare:
- [ ] **GitHub Repo:** https://github.com/yksanjo/jupiter-ai-agent ✅ (Ready)
- [ ] **README.md:** Updated with v2.0 features ✅ (Ready)
- [ ] **DX Report:** DX-REPORT.md with findings ✅ (Ready)
- [ ] **Demo Video:** Record Loom showing agent running (TODO)
- [ ] **Project Description:** Tailor for each hackathon theme (TODO)
- [ ] **Registration:** Create accounts on each platform (TODO)

### Demo Script (for Loom video):
```
1. Show GitHub repo
2. Run: python3 jupiter_ai_agent.py
3. Show output:
   - Price API: ✅ Success (SOL price fetched)
   - Multi-Price API: ✅ Success (SOL, USDC, JUP prices)
   - Swap v2 Order API: ✅ Success (swap quote generated)
   - Arbitrage Detection: ✅ Success
4. Show DX-REPORT.md
5. Explain: "This agent autonomously monitors Solana DeFi markets 
   and generates actionable developer experience feedback"
```

---

## 💰 Total Potential Earnings

| Hackathon | Best Case | Realistic |
|---|---|---|
| Surge x Kraken AI Trading | $55,000 | $2,000-5,000 |
| Solana Frontier Hackathon | $30,000 + $250K accelerator | $5,000-10,000 |
| Stellar Hacks: Agents | $10,000 | $1,000-3,000 |
| Superteam Earn Bounty | $3,000 | $1,000-3,000 |
| The Bags Hackathon | TBD | $2,000-5,000 |
| **TOTAL** | **$98,000+** | **$11,000-26,000** |

---

## 🚀 Next Steps (Manual Actions Required)

1. **IMMEDIATE (Today):**
   - Register on lablab.ai → submit to Surge x Kraken (deadline April 12)
   - Register on DoraHacks → submit to Stellar Hacks (deadline April 13)

2. **THIS WEEK:**
   - Register on colosseum.com/frontier → submit to Frontier Hackathon
   - Record Loom demo video
   - Submit to Superteam Earn via web UI

3. **THIS MONTH:**
   - Submit to The Bags Hackathon (deadline June 1)
   - Submit to Four.Meme AI Sprint (deadline April 30)
   - Submit to iExec Vibe Coding (deadline May 1)

---

## 📝 Project Descriptions (Ready to Copy-Paste)

### For AI Trading Hackathons:
```
Jupiter AI Agent v2.0 — An autonomous AI agent that monitors Solana 
token prices via Jupiter Price API v3, generates optimal swap quotes 
via Jupiter Swap v2 Order API, and detects arbitrage opportunities 
across Solana DEXs. Features include multi-price batch fetching, 
price history tracking with % change calculations, proper token 
decimal handling (SOL=9, USDC=6), and comprehensive DX reporting. 
Built in Python with only aiohttp as a dependency. All 5/5 Jupiter 
APIs tested and working.
```

### For Solana Hackathons:
```
Jupiter AI Agent v2.0 — An autonomous AI agent framework demonstrating 
how AI agents can be first-class users of Solana's DeFi infrastructure. 
The agent integrates Jupiter's entire API suite (Price v3, Swap v2, 
Token metadata) to autonomously monitor markets, detect arbitrage, 
and generate actionable developer experience feedback. Built for the 
Solana Frontier Hackathon, this project shows how AI agents can 
discover APIs through LLM-optimized docs, self-test all endpoints, 
and operate continuously with state persistence.
```

### For AI Agent Hackathons:
```
Jupiter AI Agent v2.0 — A fully autonomous AI agent that interacts 
with real-world DeFi infrastructure. Unlike chat-only agents, this 
agent makes actual API calls to Jupiter's Solana trading platform, 
fetches live token prices, generates swap quotes, detects arbitrage 
opportunities, and produces structured DX reports. It demonstrates 
practical AI agent autonomy in a production financial environment.
```

---

*Last Updated: April 11, 2026*
