def validate_inputs(symbol, side, order_type, quantity, price=None):
    if not symbol or not isinstance(symbol, str) or not symbol.isalnum():
        raise ValueError("Invalid symbol. Symbol must be alphanumeric (e.g. BTCUSDT)")

    side_upper = side.upper() if isinstance(side, str) else ""
    if side_upper not in ['BUY', 'SELL']:
        raise ValueError("Side must be either 'BUY' or 'SELL'")

    type_upper = order_type.upper() if isinstance(order_type, str) else ""
    if type_upper not in ['MARKET', 'LIMIT']:
        raise ValueError("Order type must be either 'MARKET' or 'LIMIT'")

    try:
        qty_val = float(quantity)
        if qty_val <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        raise ValueError("Quantity must be a positive number greater than 0")

    if type_upper == 'LIMIT':
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        try:
            price_val = float(price)
            if price_val <= 0:
                raise ValueError()
        except (ValueError, TypeError):
            raise ValueError("Price must be a positive number greater than 0")

    return True