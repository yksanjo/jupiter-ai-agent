# Jupiter AI Bounty Agent — v2.0

An autonomous AI agent that monitors Solana token prices, discovers arbitrage opportunities, analyzes market conditions, and generates swap quotes via Jupiter's Developer Platform APIs.

**Built for:** [Not Your Regular Bounty](https://superteam.fun/earn/hackathon/frontier) — Frontier Hackathon by Jupiter
**Author:** AI Builder Agent
**Version:** 2.0

## 🚀 Live Demo
```bash
pip install aiohttp
export JUPITER_API_KEY="your_key_here"
python3 jupiter_ai_agent.py
```

## 🤖 What This Agent Does

This is an **autonomous AI agent** that interacts with Jupiter's entire DeFi infrastructure:

- 📊 **Real-time Price Monitoring** — Track SOL, USDC, JUP, and any Solana token prices
- 🔍 **Token Discovery** — Search and discover tokens with metadata
- 🔄 **Swap Quotes** — Get optimal routing across all Solana DEXs
- 💰 **Lending Rates** — Monitor lending/borrowing rates across protocols
- 📈 **Arbitrage Detection** — Identify potential arbitrage opportunities (direct vs via SOL paths)
- 🤖 **Continuous Monitoring** — Run autonomous diagnostics with state persistence
- 📝 **DX Reports** — Generate detailed developer experience feedback

## ✨ What's New in v2.0

- **Multi-Price API** — Fetch prices for multiple tokens in single call
- **Arbitrage Detection** — Compare direct vs routed swap paths
- **Price History Tracking** — Monitor price changes over time with % calculations
- **Token Decimals Handling** — Proper decimal conversion for all major tokens
- **Enhanced Error Handling** — Better error messages and recovery
- **State Persistence** — Survives restarts with full history

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.8+ |
| HTTP | `aiohttp` (async) |
| APIs | Jupiter Price, Tokens, Swap V2, Lend |
| State | JSON file persistence |
| SSL | Custom context (macOS compatible) |

## 📡 API Endpoints Used

| API | Endpoint | Purpose |
|-----|----------|---------|
| Price | `GET /price/v2` | Real-time token prices |
| Price (Multi) | `GET /price/v2?ids=a,b,c` | Batch price fetch |
| Tokens | `GET /tokens/v1/search` | Token discovery & metadata |
| Swap V2 | `GET /swap/v2/quote` | Cross-DEX swap quotes |
| Lend | `GET /lend/rates` | Lending/borrowing rates |

## 💻 Quick Start

```bash
# Install dependencies
pip install aiohttp

# Set your Jupiter API key (get from developers.jup.ag)
export JUPITER_API_KEY="your_api_key_here"

# Run full diagnostics
python3 jupiter_ai_agent.py
```

## 🧪 Programmatic Usage

```python
from jupiter_ai_agent import JupiterAIAgent

agent = JupiterAIAgent()

# Get single token price
price = await agent.get_token_price("So11111111111111111111111111111111111111112")

# Get multiple prices at once
prices = await agent.get_multiple_prices([SOL_MINT, USDC_MINT, JUP_MINT])

# Search for tokens
tokens = await agent.search_tokens("SOL")

# Get swap quote (1 SOL → USDC)
quote = await agent.get_swap_quote(SOL_MINT, USDC_MINT, 1000000000)

# Check for arbitrage opportunities
arb = await agent.find_arbitrage_opportunity(SOL_MINT, USDC_MINT, 1000000000)

# Monitor tokens over time
await agent.monitor_tokens([SOL_MINT, USDC_MINT], iterations=10, interval=30)

# Run full diagnostic suite
results = await agent.run_full_diagnostics()
```

## 📊 Agent Autonomy Features

This agent operates independently without human intervention:

1. **API Health Monitoring** — Tests all endpoints on each run
2. **State Persistence** — Saves/loads state across restarts
3. **Price History** — Maintains rolling price history (last 100 points)
4. **Error Recovery** — Handles network failures gracefully
5. **Automated Reports** — Generates structured DX feedback

## 🎯 Why This Is Novel

This is **not** just another trading bot. It's an **AI agent framework** demonstrating:

1. **LLM-Optimized API Consumption** — Uses `llms.txt` for autonomous API discovery
2. **Self-Testing Architecture** — Validates all endpoints automatically
3. **Multi-Path Analysis** — Compares direct vs routed swap paths for arbitrage
4. **Developer Experience Feedback** — Generates actionable reports for API improvement
5. **Zero-Config Operation** — Works out of the box with just an API key

## 🔗 Links

- **Jupiter Developer Platform:** https://dev.jup.ag
- **Frontier Hackathon:** https://superteam.fun/earn/hackathon/frontier
- **Superteam Earn:** https://earn.superteam.fun
- **GitHub Repository:** https://github.com/yksanjo/jupiter-ai-agent

## 📄 DX Report

See [DX-REPORT.md](./DX-REPORT.md) for detailed feedback on integrating with Jupiter's Developer Platform.

## 📋 Bounty Submission Checklist

- [x] Jupiter Price API integration
- [x] Jupiter Tokens API integration
- [x] Jupiter Swap V2 API integration
- [x] Jupiter Lend API integration
- [x] Autonomous diagnostics suite
- [x] State persistence
- [x] DX Report generation
- [x] Arbitrage detection (v2.0)
- [x] Multi-price batch fetch (v2.0)
- [x] Price history tracking (v2.0)

## 📜 License

MIT

---

*Built during the Solana Frontier Hackathon 2026. All code is open-source and available for reuse.*
