import os
from binance.client import Client
from binance.enums import *
from bot.logging_config import logger
from dotenv import load_dotenv

load_dotenv()

class OrderManager:
    def init(self):
        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")
        
        if not api_key or not api_secret:
            raise ValueError("API Key and Secret not found in .env file")

        # IMPORTANT: Futures Testnet er jonno direct URL diye client banacchi
        self.client = Client(
            api_key=api_key, 
            api_secret=api_secret,
            tld='com'
        )
        # Demo Testnet URL force kora
        self.client.FUTURES_URL = 'https://testnet.binancefuture.com'
        
        logger.info("Connected to Binance Futures Testnet")

    def execute_order(self, symbol, side, order_type, quantity, price=None):
        try:
            # Futures e symbol format: BTCUSDT
            symbol = symbol.upper()
            
            if order_type == "MARKET":
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=FUTURE_ORDER_TYPE_MARKET,
                    quantity=quantity
                )
            elif order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price is required for LIMIT orders")
                order = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type=FUTURE_ORDER_TYPE_LIMIT,
                    timeInForce=TIME_IN_FORCE_GTC,
                    quantity=quantity,
                    price=str(price)
                )
            else:
                raise ValueError("Invalid order type")
            
            logger.info(f"Order Placed: {order}")
            return order
            
        except Exception as e:
            logger.error(f"Order execution failed: {e}")
            raise e