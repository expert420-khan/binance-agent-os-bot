import requests

# 1. Binance live market data
url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
data = requests.get(url).json()
price = float(data['price'])

# 2. Agent Decision
if price > 60000:
    signal = "BULLISH (Buy Signal)"
else:
    signal = "NEUTRAL (Hold)"

# 3. Output
print("--- BINANCE AGENT OS WORKFLOW ---")
print(f"Coin: BTC/USDT")
print(f"Live Price: ${price}")
print(f"AI Decision: {signal}")
print("Status: Workflow Executed Successfully!")
