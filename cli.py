import argparse
import sys
from bot.orders import OrderManager

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet CLI Trading Bot")
    parser.add_argument("--symbol", required=True, type=str, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, type=str, choices=["BUY", "SELL", "buy", "sell"], help="Order side (BUY/SELL)")
    parser.add_argument("--type", required=True, type=str, choices=["MARKET", "LIMIT", "market", "limit"], help="Order type (MARKET/LIMIT)")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, default=None, help="Order price (Required for LIMIT orders)")

    args = parser.parse_args()

    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = args.quantity
    price = args.price

    try:
        order_manager = OrderManager()
        order = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        order_id = order.get("orderId", "N/A")
        order_symbol = order.get("symbol", symbol)
        order_side = order.get("side", side)
        order_status = order.get("status", "N/A")

        print("\n" + "=" * 45)
        print("          ORDER PLACED SUCCESSFULLY          ")
        print("=" * 45)
        print(f"  Order ID : {order_id}")
        print(f"  Symbol   : {order_symbol}")
        print(f"  Side     : {order_side}")
        print(f"  Status   : {order_status}")
        print("=" * 45 + "\n")

    except Exception as e:
        print(f"\n[ERROR] Order placement failed: {e}\n", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()