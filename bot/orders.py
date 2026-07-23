from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.client import BinanceFuturesClient
from bot.config import logger
from bot.validators import validate_inputs

class OrderManager:
    def __init__(self):
        self.bot_client = BinanceFuturesClient()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            validate_inputs(symbol, side, order_type, quantity, price)

            logger.info(f"Preparing Order - Symbol: {symbol}, Side: {side}, Type: {order_type}, Quantity: {quantity}, Price: {price}")

            order_response = self.bot_client.create_order(
                symbol=symbol,
                side=side,
                order_type=order_type,
                quantity=quantity,
                price=price
            )

            logger.info(f"Order Executed Successfully. Response: {order_response}")
            return order_response

        except BinanceAPIException as e:
            logger.error(f"Binance API Error: Code {e.code} - {e.message}")
            raise RuntimeError(f"Binance API Error [{e.code}]: {e.message}")
        except BinanceRequestException as e:
            logger.error(f"Binance Request Error: {e}")
            raise RuntimeError(f"Network / Request Error: {e}")
        except ValueError as e:
            logger.error(f"Validation Error: {e}")
            raise e
        except Exception as e:
            logger.error(f"Unexpected Error during order execution: {e}")
            raise RuntimeError(f"Unexpected Error: {e}")
