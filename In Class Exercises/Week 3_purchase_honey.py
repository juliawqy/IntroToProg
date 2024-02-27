import week3_retail_utility

spend_limit = int(input("How much do you want to spend? $"))

onekg = week3_retail_utility.calculate_max_quantity_and_change(98.5, spend_limit)
spend_limit = onekg[1]

halfkg = week3_retail_utility.calculate_max_quantity_and_change(58.5, spend_limit)
change = halfkg[1]

amount = onekg[0]*1000 + halfkg[0]*500

print(f"You can buy {amount}g of honey. You have ${change} left as your change.")