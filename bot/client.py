import os
import time
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()

class BinanceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        if not api_key or not api_secret:
            raise ValueError("BINANCE_API_KEY or BINANCE_API_SECRET not found in .env file.")

        self.client = Client(
            api_key=api_key,
            api_secret=api_secret,
            testnet=True
        )
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com'

        # Sync local time offset with Binance Futures server time (fixes error -1021)
        try:
            res = self.client.futures_time()
            server_time = res.get('serverTime')
            if server_time:
                local_time = int(time.time() * 1000)
                self.client.timestamp_offset = server_time - local_time
        except Exception:
            pass

    def create_order(self, symbol, side, order_type, quantity, price=None):
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': float(quantity),
            'recvWindow': 60000
        }

        if order_type.upper() == 'LIMIT':
            if price is None:
                raise ValueError("Price is required for LIMIT order")
            params['price'] = str(price)
            params['timeInForce'] = 'GTC'

        return self.client.futures_create_order(**params)