#!/usr/bin/env python3
"""
Jupiter AI Bounty Agent
An autonomous AI agent that integrates with Jupiter's Developer Platform APIs
for token discovery, price monitoring, swap quotes, and lending rate analysis.

Built for: "Not Your Regular Bounty" - Frontier Hackathon
Author: AI Builder Agent
"""

import os
import json
import asyncio
import aiohttp
import ssl
from datetime import datetime
from pathlib import Path

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

class JupiterAIAgent:
    """Autonomous AI agent for interacting with Jupiter DeFi platform"""
    
    def __init__(self):
        self.api_key = JUPITER_API_KEY
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.state = self.load_state()
        
    def load_state(self):
        if STATE_FILE.exists():
            return json.loads(STATE_FILE.read_text())
        return {
            "created_at": datetime.now().isoformat(),
            "total_api_calls": 0,
            "successful_calls": 0,
            "failed_calls": 0,
            "api_results": {}
        }
    
    def save_state(self):
        STATE_FILE.write_text(json.dumps(self.state, indent=2))
    
    async def api_call(self, endpoint: str, params: dict = None) -> dict:
        """Make an API call to Jupiter with error handling"""
        url = f"{JUPITER_API_BASE}{endpoint}"
        try:
            connector = aiohttp.TCPConnector(ssl=ssl_context)
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get(url, headers=self.headers, params=params) as resp:
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
    
    async def get_price(self, token_mint: str) -> dict:
        """Get token price via Jupiter Price API"""
        print(f"💰 Fetching price for {token_mint[:8]}...")
        result = await self.api_call("/price/v2", {"ids": token_mint})
        self.state["api_results"]["price"] = result
        return result
    
    async def search_tokens(self, query: str) -> dict:
        """Search tokens via Jupiter Tokens API"""
        print(f"🔍 Searching tokens for '{query}'...")
        result = await self.api_call("/tokens/v1/search", {"query": query, "limit": 5})
        self.state["api_results"]["token_search"] = result
        return result
    
    async def get_swap_quote(self, input_mint: str, output_mint: str, amount: int) -> dict:
        """Get swap quote via Jupiter Swap V2 API"""
        print(f"🔄 Getting swap quote: {input_mint[:8]} → {output_mint[:8]}...")
        params = {
            "inputMint": input_mint,
            "outputMint": output_mint,
            "amount": amount,
            "slippageBps": 50
        }
        result = await self.api_call("/swap/v2/quote", params)
        self.state["api_results"]["swap_quote"] = result
        return result
    
    async def get_lend_rates(self) -> dict:
        """Get lending rates via Jupiter Lend API"""
        print("💵 Fetching lending rates...")
        result = await self.api_call("/lend/rates")
        self.state["api_results"]["lend_rates"] = result
        return result
    
    async def run_full_diagnostics(self):
        """Test all Jupiter APIs and compile comprehensive DX report"""
        print("\n" + "="*70)
        print("🧪 Jupiter API Full Diagnostic Suite")
        print("="*70 + "\n")
        
        results = {}
        
        # Test 1: Price API
        print("[1/4] Testing Price API...")
        price_result = await self.get_price(SOL_MINT)
        results["price_api"] = {
            "status": "✅ Success" if price_result["status"] == "success" else f"❌ HTTP {price_result.get('http_status', 'Error')}",
            "response": price_result
        }
        print(f"       Result: {results['price_api']['status']}")
        
        # Test 2: Token Search
        print("[2/4] Testing Token Search API...")
        search_result = await self.search_tokens("SOL")
        results["token_api"] = {
            "status": "✅ Success" if search_result["status"] == "success" else f"❌ HTTP {search_result.get('http_status', 'Error')}",
            "response": search_result
        }
        print(f"       Result: {results['token_api']['status']}")
        
        # Test 3: Swap Quote
        print("[3/4] Testing Swap V2 API...")
        swap_result = await self.get_swap_quote(SOL_MINT, USDC_MINT, 1000000)
        results["swap_api"] = {
            "status": "✅ Success" if swap_result["status"] == "success" else f"❌ HTTP {swap_result.get('http_status', 'Error')}",
            "response": swap_result
        }
        print(f"       Result: {results['swap_api']['status']}")
        
        # Test 4: Lend API
        print("[4/4] Testing Lend API...")
        lend_result = await self.get_lend_rates()
        results["lend_api"] = {
            "status": "✅ Success" if lend_result["status"] == "success" else f"❌ HTTP {lend_result.get('http_status', 'Error')}",
            "response": lend_result
        }
        print(f"       Result: {results['lend_api']['status']}")
        
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
        
        self.save_state()
        return results


async def main():
    """Main entry point"""
    agent = JupiterAIAgent()
    await agent.run_full_diagnostics()

if __name__ == "__main__":
    asyncio.run(main())
