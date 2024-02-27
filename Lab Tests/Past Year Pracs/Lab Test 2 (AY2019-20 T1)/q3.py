# Name:
# Email ID:

def compute_total_price(price_dict, item_list):
    # Modify the code below.

    total_price = 0.0

    for items in item_list:
        if items[0] in price_dict:
            total_price += price_dict[items[0]]*items[1]

    return total_price