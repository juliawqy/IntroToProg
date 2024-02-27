def calculate_max_quantity_and_change(unit_price, amount):
    max_quantity = int(amount//unit_price)
    change = amount%unit_price
    return max_quantity, change