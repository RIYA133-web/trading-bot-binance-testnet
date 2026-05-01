print("File started")
from binance.client import Client
print("binance client imported successfully")
from config import API_KEY, API_SECRET, BASE_URL
class BinanceClient:
    def __init__(self):
        self.client = Client(API_KEY, API_SECRET,testnet=True)
        
    def get_client(self):
        return self.client    
    