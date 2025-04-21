'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
from decimal import Decimal, InvalidOperation, getcontext

getcontext().prec = 28

Order = namedtuple('Order', 'id, items')
Item  = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    MAX_ORDER_VOLUME = Decimal('1000000')
    net              = Decimal('0')
    volume           = Decimal('0')

    for item in order.items:
        if not isinstance(item.amount, (int, float)):
            return "Invalid amount"

        try:
            amt = Decimal(str(item.amount))
        except (InvalidOperation, ValueError):
            return "Invalid amount"

        if item.type == 'payment':
            net    += amt
            volume += abs(amt)

        elif item.type == 'product':
            if not isinstance(item.quantity, int):
                return "Invalid quantity"

            subtotal = amt * item.quantity
            net     -= subtotal
            volume  += abs(subtotal)

        else:
            return f"Invalid item type: {item.type}"

    if net == 0 and volume > MAX_ORDER_VOLUME:
        return "Total amount payable for an order exceeded"

    if net != 0:
        return f"Order ID: {order.id} - Payment imbalance: ${net:0.2f}"

    return f"Order ID: {order.id} - Full payment received!"