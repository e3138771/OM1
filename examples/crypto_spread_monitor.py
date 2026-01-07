# OM1 Community Example: Crypto Price Spread Monitor
# This agent monitors the Z-Score spread between BTC/ETH 

import requests
import time

def get_spread():
    # 使用 OKX 作為基準 API (符合 OM1 的 Web3 背景)
    btc = float(requests.get("https://www.okx.com/api/v5/market/ticker?instId=BTC-USDT").json()['data'][0]['last'])
    eth = float(requests.get("https://www.okx.com/api/v5/market/ticker?instId=ETH-USDT").json()['data'][0]['last'])
    return btc / eth

if __name__ == "__main__":
    print("🚀 OM1 Crypto Monitor Starting...")
    # 這裡可以加入我們之前的 Z-Score 邏輯
    print(f"Current BTC/ETH Ratio: {get_spread():.4f}")
