from binance.client import Client

client = Client("your_api_key", "your_secret", testnet=True)

print(client.futures_account_balance())