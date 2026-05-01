# Binance Futures Testnet Trading Bot

## 🚀 Features
- Place MARKET and LIMIT orders
- Supports BUY and SELL
- CLI-based input using argparse
- Logging to file
- Error handling and validation

## ⚙️ Setup

1. Install dependencies:
pip install -r requirements.txt

2. Add API keys in config.py

3. Run MARKET order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

4. Run LIMIT order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000

## 📁 Logs
Check trading_bot.log for request/response logs

## ⚠️ Notes
- Uses Binance Futures Testnet (no real money)
- API keys should not be shared publicly