# Binance Futures Testnet Trading Bot

## Setup
1. pip install -r requirements.txt
2. Create .env file with BINANCE_API_KEY and BINANCE_API_SECRET from https://testnet.binancefuture.com
3. Make sure you have testnet USDT

## How to Run
Market Order:
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

Limit Order:
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000

## Assumptions
- Using USDT-M Futures Testnet
- Quantity in base asset e.g. BTC
- Logs saved in logs/bot.log