# Binance Futures Testnet CLI Trading Bot

A Command Line Interface (CLI) trading bot written in Python for placing orders on **Binance Futures Testnet**.

## Project Structure
```text
Test Bot/
├── bot/
│   ├── client.py        # Binance Testnet Client setup
│   ├── config.py        # Logging configuration (logs/trading.log)
│   ├── orders.py        # Order management & execution
│   └── validators.py    # CLI & order parameter validation
├── .env                 # API Keys configuration
├── cli.py               # Main CLI Entry Point (argparse)
├── requirements.txt     # Dependencies
└── README.md            # Documentation
```

## Setup & Installation

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   Update `.env` file with your Binance Futures Testnet API Key and Secret:
   ```env
   BINANCE_API_KEY=your_api_key_here
   BINANCE_API_SECRET=your_api_secret_here
   ```
   > Get testnet keys from [Binance Futures Testnet](https://testnet.binancefuture.com).

## Usage Examples

### 1. Market Order
Place a Market BUY order for `0.001` BTCUSDT:
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### 2. Limit Order
Place a Limit SELL order for `0.001` BTCUSDT at price `$70,000`:
```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

## Logging & Error Handling
- All logs and raw order responses are saved automatically in `logs/trading.log`.
- Input validation prevents invalid requests before sending to Binance API.
- Comprehensive exception handling catches API, Network, and Parameter errors.