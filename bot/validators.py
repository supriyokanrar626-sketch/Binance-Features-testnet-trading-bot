def validate_inputs(symbol, side, order_type, quantity, price):
    if not symbol.isalnum():
        raise ValueError("Invalid symbol")
    if side not in ['BUY', 'SELL']:
        raise ValueError("Side must be BUY or SELL")
    if order_type not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be MARKET or LIMIT")
    if float(quantity) <= 0:
        raise ValueError("Quantity must be > 0")
    if order_type == 'LIMIT' and (not price or float(price) <= 0):
        raise ValueError("Price is required for LIMIT order")
    return True