# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

def get_promotion(food_category):
    # Replace the code below with your implementation.

    if food_category == "vegetable" or food_category == 'vegetables':
        return "5%"
    elif food_category == "fruits" or food_category == 'fruits':
        return "7.5%"
    elif food_category == "seasoning" or food_category == 'seasonings':
        return "3%"
    elif food_category == "flour" or food_category == 'flours':
        return "10%"
    else:
        return 'No Promotion'
