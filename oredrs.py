from .client import BinanceClient
from .validators import validate_inputs
from .logging_config import logger

class OrderManager:
    def init(self):
        self.client = BinanceClient()
    
    def execute_order(self, symbol, side, order_type, quantity, price=None):
        validate_inputs(symbol, side, order_type, quantity, price)
        
        print("\n--- ORDER REQUEST SUMMARY ---")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price: print(f"Price: {price}")
        print("-----------------------------\n")
        
        response = self.client.place_order(symbol, side, order_type, quantity, price)
        
        print("--- ORDER RESPONSE ---")
        print(f"OrderId: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Executed Qty: {response['executedQty']}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        print("----------------------")
        return response
    
    def place_stop_limit(self, symbol, side, quantity, price, stopPrice):
     return self.client.futures_create_order(
        symbol=symbol, side=side, type='STOP', 
        quantity=quantity, price=price, stopPrice=stopPrice, timeInForce='GTC'
     )