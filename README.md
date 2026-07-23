# Binance Futures Testnet Trading Bot

A simple command-line Python bot to place MARKET and LIMIT orders on Binance Futures Testnet.

## Features
- Place MARKET and LIMIT orders via CLI
- Uses Binance Futures Testnet API
- Structured code with separate API and CLI layers
- Logging of all API requests, responses, and errors to logs/
- Exception handling for invalid input, API errors, and network failures
- Clear output with order summary and response details

## Setup Steps

1.  Clone the repository
    `bash
    git clone : https://github.com/supriyokanrar626-sketch/Binance-Features-testnet-trading-bot)

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
