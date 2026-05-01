def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")


def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")


def validate_quantity(qty):
    try:
        qty = float(qty)
    except:
        raise ValueError("Quantity must be a number")

    if qty <= 0:
        raise ValueError("Quantity must be greater than 0")


def validate_price(price, order_type):
    order_type = order_type.upper()

    # Only validate price for LIMIT orders
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT order")

        try:
            price = float(price)
        except:
            raise ValueError("Price must be a number")

        if price <= 0:
            raise ValueError("Price must be greater than 0")