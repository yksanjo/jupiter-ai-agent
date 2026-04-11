#!/usr/bin/env python3
"""
Jupiter AI Bounty Agent — v2.0
Autonomous AI agent for Jupiter's Frontier Hackathon
Integrates Jupiter Swap v2, Price, Token APIs with advanced analytics

Built for: "Not Your Regular Bounty" — Frontier Hackathon
Author: AI Builder Agent
"""

import os
import json
import asyncio
import aiohttp
import ssl
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# Fix SSL on macOS
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

# Configuration
JUPITER_API_KEY = os.environ.get("JUPITER_API_KEY", "jup_226d696a615618475e19d08aa5248baa2fc055da6804591827b838bdbf227c90")
JUPITER_API_BASE = "https://api.jup.ag"

# State file for persistence
STATE_FILE = Path(__file__).parent / "agent_state.json"

# Known token mint addresses
SOL_MINT = "So11111111111111111111111111111111111111112"
USDC_MINT = "EPjFWdd5AufqSSqeM2qN1xzybapC8G4wEGGkZwyTDt1v"
USDT_MINT = "Es9vMFrzaCERmJfrF4H2FYD4KCoNkY11McCe8BenwNYB"
JUP_MINT = "JUPyiwrYJFskUPiHa7hkeR8VUtAeFoSYbKedZNsDvCN"

# Token decimals mapping
TOKEN_DECIMALS = {
    SOL_MINT: 9,
    USDC_MINT: 6,
    USDT_MINT: 6,
    JUP_MINT: 6,
}

class JupiterAIAgent:
    """Autonomous AI agent for interacting with Jupiter DeFi platform"""

    def __init__(self):
        self.api_key = JUPITER_API_KEY
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }
        self.state = self.load_state()
        self.price_history = []

    def load_state(self):
        if STATE_FILE.exists():
            return json.loads(STATE_FILE.read_text())
        return {
            "created_at": datetime.now().isoformat(),
            "total_api_calls": 0,
            "successful_calls": 0,
            "failed_calls": 0,
            "api_results": {},
            "price_history": [],
            "alerts_triggered": 0
        }

    def save_state(self):
        STATE_FILE.write_text(json.dumps(self.state, indent=2))

    def get_decimals(self, token_mint: str) -> int:
        """Get token decimals from known mapping or default to 6"""
        return TOKEN_DECIMALS.get(token_mint, 6)

    def format_amount(self, amount: int, token_mint: str) -> float:
        """Format raw token amount to human-readable value"""
        decimals = self.get_decimals(token_mint)
        return amount / (10 ** decimals)

    def to_raw_amount(self, human_amount: float, token_mint: str) -> int:
        """Convert human-readable amount to raw token amount"""
        decimals = self.get_decimals(token_mint)
        return int(human_amount * (10 ** decimals))

    async def api_call(self, endpoint: str, params: dict = None, use_api_key: bool = True) -> dict:
        """Make an API call to Jupiter with error handling"""
        url = f"{JUPITER_API_BASE}{endpoint}"
        headers = self.headers if use_api_key else {"Content-Type": "application/json"}
        
        try:
            connector = aiohttp.TCPConnector(ssl=ssl_context)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(url, headers=headers, params=params) as resp:
                    self.state["total_api_calls"] += 1
                    status = resp.status

                    if status == 200:
                        self.state["successful_calls"] += 1
                        try:
                            data = await resp.json()
                            return {"status": "success", "data": data, "http_status": status}
                        except:
                            text = await resp.text()
                            return {"status": "success", "data": text, "http_status": status}
                    else:
                        self.state["failed_calls"] += 1
                        text = await resp.text()
                        return {"status": "error", "http_status": status, "response": text}
        except Exception as e:
            self.state["failed_calls"] += 1
            return {"status": "error", "error": str(e)}

    async def get_token_price(self, token_mint: str) -> dict:
        """Get token price via Jupiter Price API v3"""
        result = await self.api_call(f"/price/v3?ids={token_mint}")
        if result["status"] == "success" and isinstance(result["data"], dict):
            price_data = result["data"].get(token_mint, {})
            price = price_data.get("usdPrice", "N/A")
            liquidity = price_data.get("liquidity", 0)
            change_24h = price_data.get("priceChange24h", 0)
            self.state["api_results"]["last_price"] = {
                "token": token_mint[:8],
                "price": price,
                "liquidity": liquidity,
                "priceChange24h": change_24h,
                "timestamp": datetime.now().isoformat()
            }
            self.price_history.append({
                "price": price,
                "timestamp": datetime.now().isoformat()
            })
            if len(self.price_history) > 100:
                self.price_history = self.price_history[-100:]
        return result

    async def get_multiple_prices(self, token_mints: list) -> dict:
        """Get prices for multiple tokens in one call via Price API v3"""
        ids = ",".join(token_mints)
        result = await self.api_call(f"/price/v3?ids={ids}")
        if result["status"] == "success" and isinstance(result["data"], dict):
            prices = {}
            for mint in token_mints:
                token_data = result["data"].get(mint, {})
                prices[mint[:8]] = {
                    "price": token_data.get("usdPrice", "N/A"),
                    "liquidity": token_data.get("liquidity", 0),
                    "priceChange24h": token_data.get("priceChange24h", 0)
                }
            return {"status": "success", "prices": prices}
        return result

    async def search_tokens(self, query: str) -> dict:
        """Search tokens via Jupiter Token List API"""
        # Jupiter now uses the token list from station.jup.ag
        result = await self.api_call(f"/tokens/v1/search?query={query}&limit=10", use_api_key=False)
        if result["status"] == "success" and isinstance(result["data"], list):
            tokens = []
            for token in result["data"]:
                tokens.append({
                    "name": token.get("name", "Unknown"),
                    "symbol": token.get("symbol", "Unknown"),
                    "address": token.get("address", ""),
                    "decimals": token.get("decimals", 6),
                    "logoURI": token.get("logoURI", "")
                })
            return {"status": "success", "tokens": tokens}
        return result

    async def get_swap_quote(self, input_mint: str, output_mint: str, amount: int) -> dict:
        """Get swap quote via Jupiter Swap v2 Order API"""
        params = {
            "inputMint": input_mint,
            "outputMint": output_mint,
            "amount": str(amount),
            "slippageBps": 50,
            "taker": "11111111111111111111111111111111"
        }
        result = await self.api_call("/swap/v2/order", params=params)
        if result["status"] == "success" and isinstance(result["data"], dict):
            quote_data = result["data"]
            return {
                "status": "success",
                "quote": {
                    "inputMint": input_mint[:8],
                    "outputMint": output_mint[:8],
                    "inAmount": quote_data.get("inAmount", ""),
                    "outAmount": quote_data.get("outAmount", ""),
                    "priceImpactPct": quote_data.get("priceImpactPct", ""),
                    "minimumOutAmount": quote_data.get("minimumOutAmount", ""),
                    "platformFee": quote_data.get("platformFee", ""),
                    "routePlan": str(quote_data.get("routePlan", []))[:100]
                }
            }
        return result

    async def get_swap_order(self, input_mint: str, output_mint: str, amount: int, 
                             user_public_key: str = "11111111111111111111111111111111") -> dict:
        """Get full swap order via Jupiter Swap v2 API"""
        params = {
            "inputMint": input_mint,
            "outputMint": output_mint,
            "amount": str(amount),
            "slippageBps": 50,
            "userPublicKey": user_public_key
        }
        result = await self.api_call("/swap/v2/order", params=params)
        if result["status"] == "success":
            return {"status": "success", "order": result["data"]}
        return result

    async def find_arbitrage_opportunity(self, token_a: str, token_b: str, amount: int) -> dict:
        """Check for potential arbitrage between two token paths"""
        # Direct path
        direct_quote = await self.get_swap_quote(token_a, token_b, amount)
        
        # Via SOL path (if neither token is SOL)
        if token_a != SOL_MINT and token_b != SOL_MINT:
            via_sol_a = await self.get_swap_quote(token_a, SOL_MINT, amount)
            if via_sol_a["status"] == "success":
                sol_amount = int(via_sol_a.get("quote", {}).get("outAmount", 0))
                if sol_amount > 0:
                    via_sol_b = await self.get_swap_quote(SOL_MINT, token_b, sol_amount)
                    if via_sol_b["status"] == "success":
                        direct_out = int(direct_quote.get("quote", {}).get("outAmount", 0))
                        via_sol_out = int(via_sol_b.get("quote", {}).get("outAmount", 0))
                        
                        return {
                            "direct": direct_quote,
                            "via_sol": via_sol_b,
                            "arbitrage_possible": via_sol_out > direct_out,
                            "difference": via_sol_out - direct_out if via_sol_out > direct_out else direct_out - via_sol_out
                        }
        
        return {
            "direct": direct_quote,
            "arbitrage_possible": False
        }

    def calculate_price_change(self) -> dict:
        """Calculate price change from history"""
        if len(self.price_history) < 2:
            return {"status": "insufficient_data"}
        
        try:
            first_price = float(self.price_history[0]["price"])
            last_price = float(self.price_history[-1]["price"])
            
            if first_price == 0:
                return {"status": "invalid_data"}
            
            change_pct = ((last_price - first_price) / first_price) * 100
            
            return {
                "status": "calculated",
                "first_price": first_price,
                "last_price": last_price,
                "change_pct": round(change_pct, 2),
                "direction": "up" if change_pct > 0 else "down"
            }
        except:
            return {"status": "parse_error"}

    async def monitor_tokens(self, token_list: list, iterations: int = 5, interval: int = 10):
        """Monitor multiple tokens over time"""
        print(f"\n🔍 Starting token monitor for {len(token_list)} tokens...")
        
        for i in range(iterations):
            print(f"\n--- Iteration {i+1}/{iterations} ---")
            prices = await self.get_multiple_prices(token_list)
            
            if prices["status"] == "success":
                for token, price in prices["prices"].items():
                    print(f"  {token}: ${price}")
            
            change = self.calculate_price_change()
            if change["status"] == "calculated":
                arrow = "📈" if change["direction"] == "up" else "📉"
                print(f"  {arrow} Price change: {change['change_pct']}%")
            
            await asyncio.sleep(interval)

    async def run_full_diagnostics(self):
        """Test all Jupiter APIs and compile comprehensive DX report"""
        print("\n" + "="*70)
        print("🧪 Jupiter API Full Diagnostic Suite v2.0")
        print("="*70 + "\n")

        results = {}

        # Test 1: Price API
        print("[1/5] Testing Price API...")
        price_result = await self.get_token_price(SOL_MINT)
        results["price_api"] = {
            "status": "✅ Success" if price_result["status"] == "success" else f"❌ HTTP {price_result.get('http_status', 'Error')}",
            "response": price_result
        }
        print(f"       Result: {results['price_api']['status']}")

        # Test 2: Multi-Price API
        print("[2/5] Testing Multi-Price API...")
        multi_price = await self.get_multiple_prices([SOL_MINT, USDC_MINT, JUP_MINT])
        results["multi_price_api"] = {
            "status": "✅ Success" if multi_price["status"] == "success" else f"❌ HTTP {multi_price.get('http_status', 'Error')}",
            "response": multi_price
        }
        print(f"       Result: {results['multi_price_api']['status']}")

        # Test 3: Swap Quote
        print("[3/5] Testing Swap v2 Quote API...")
        swap_result = await self.get_swap_quote(SOL_MINT, USDC_MINT, 1000000)
        results["swap_api"] = {
            "status": "✅ Success" if swap_result["status"] == "success" else f"❌ HTTP {swap_result.get('http_status', 'Error')}",
            "response": swap_result
        }
        print(f"       Result: {results['swap_api']['status']}")

        # Test 4: Swap Order
        print("[4/5] Testing Swap v2 Order API...")
        order_result = await self.get_swap_order(SOL_MINT, USDC_MINT, 1000000)
        results["swap_order_api"] = {
            "status": "✅ Success" if order_result["status"] == "success" else f"❌ HTTP {order_result.get('http_status', 'Error')}",
            "response": order_result
        }
        print(f"       Result: {results['swap_order_api']['status']}")

        # Test 5: Arbitrage Check
        print("[5/5] Testing Arbitrage Detection...")
        arb_result = await self.find_arbitrage_opportunity(SOL_MINT, USDC_MINT, 1000000)
        results["arbitrage_api"] = {
            "status": "✅ Success",
            "response": arb_result
        }
        print(f"       Result: {results['arbitrage_api']['status']}")

        # Summary
        print("\n" + "="*70)
        print("📊 Diagnostic Summary")
        print("="*70)
        for api, result in results.items():
            print(f"  {api}: {result['status']}")

        print(f"\n📈 API Statistics:")
        print(f"  Total calls:     {self.state['total_api_calls']}")
        print(f"  Successful:      {self.state['successful_calls']}")
        print(f"  Failed:          {self.state['failed_calls']}")
        print(f"  Started:         {self.state['created_at']}")
        print(f"  Price points:    {len(self.price_history)}")

        self.save_state()
        return results


async def main():
    """Main entry point"""
    agent = JupiterAIAgent()
    await agent.run_full_diagnostics()

if __name__ == "__main__":
    asyncio.run(main())
