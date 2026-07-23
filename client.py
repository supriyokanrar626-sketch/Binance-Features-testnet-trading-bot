from binance.client import Client
from binance.exceptions import BinanceAPIException
from dotenv import load_dotenv
import os
from .logging_config import logger

load_dotenv()

class BinanceClient:
    def init(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        self.client = Client(api_key, api_secret, testnet=True)
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com'
        logger.info("Binance Testnet Client Initialized")

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol,
                'side': side,
                'type': order_type,
                'quantity': quantity
            }
            if order_type == 'LIMIT':
                params['price'] = price
                params['timeInForce'] = 'GTC'
            
            logger.info(f"Placing Order: {params}")
            order = self.client.futures_create_order(**params)
            logger.info(f"Order Response: {order}")
            return order
        except BinanceAPIException as e:
            logger.error(f"Binance API Error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected Error: {e}")
            raise