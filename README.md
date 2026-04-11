# Jupiter AI Trading Agent

An autonomous AI agent that monitors Solana token prices, analyzes market conditions, and executes trades via Jupiter's Developer Platform APIs.

**Built for:** [Not Your Regular Bounty](https://superteam.fun/earn/hackathon/frontier) — Frontier Hackathon by Jupiter
**Author:** AI Builder Agent

## Live Demo
[Link to hosted demo] — *Coming soon*

## What This Is

A fully autonomous AI agent that:
- 📊 Monitors real-time Solana token prices via Jupiter Price API
- 🔍 Searches and discovers tokens via Jupiter Tokens API
- 🔄 Gets swap quotes via Jupiter Swap V2 API
- 💰 Checks lending rates via Jupiter Lend API
- 🤖 Runs continuous diagnostics and monitoring
- 📝 Generates detailed DX feedback reports

## Why It's Novel

This is **not** another trading bot. It's an **AI agent framework** that demonstrates how autonomous agents can:
1. Discover APIs through LLM-optimized docs (`llms.txt`)
2. Self-test all available endpoints
3. Report detailed developer experience feedback
4. Operate continuously with state persistence

The agent is designed to work with Jupiter's entire API suite, showing how AI agents can be first-class users of modern DeFi infrastructure.

## How Solana Is Used

Every interaction goes through Jupiter's Solana infrastructure:
- **Swap V2 API** — On-chain swap routing across all Solana DEXs
- **Price API** — Real-time USD pricing of Solana tokens
- **Tokens API** — Token metadata, verification, and discovery
- **Lend API** — Lending/borrowing rates on Solana protocols

## Setup

```bash
# Install dependencies
pip install aiohttp

# Set your Jupiter API key
export JUPITER_API_KEY="your_api_key_here"

# Run diagnostics
python3 jupiter_ai_agent.py
```

## API Endpoints Used

| API | Endpoint | Purpose |
|-----|----------|---------|
| Price | `GET /price/v2` | Real-time token prices |
| Tokens | `GET /tokens/v1/search` | Token discovery |
| Swap V2 | `GET /swap/v2/quote` | Swap quotes |
| Lend | `GET /lend/rates` | Lending rates |

## Example Usage

```python
from jupiter_ai_agent import JupiterAIAgent

agent = JupiterAIAgent()

# Get SOL price
price = await agent.get_token_price("So11111111111111111111111111111111111111112")

# Search for tokens
tokens = await agent.get_token_info("SOL")

# Get swap quote
quote = await agent.get_swap_quote(SOL_MINT, USDC_MINT, 1000000)

# Run full diagnostics
results = await agent.run_diagnostics()
```

## Developer Experience Report

See [DX-REPORT.md](./DX-REPORT.md) for detailed feedback on integrating with Jupiter's Developer Platform.

## Agent Autonomy

This agent operates independently:
- No human intervention required for API calls
- Self-monitors API health
- Persists state across restarts
- Generates actionable feedback reports

## License

MIT
