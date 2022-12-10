import time
import requests

# Your IEX Cloud API token
api_token = "YOUR_API_TOKEN_HERE"

while True:
  # Fetch the top 10 stocks from the IEX Cloud API
  response = requests.get(f"https://cloud.iexapis.com/stable/stock/market/list/mostactive?token={api_token}")

  # Parse the JSON response
  stocks = response.json()

  # Print the stock data
  for stock in stocks[:10]:
    print(f"{stock['symbol']}: {stock['latestPrice']}")

  # Wait for 1 second before fetching the next batch of stock data
  time.sleep(1)
