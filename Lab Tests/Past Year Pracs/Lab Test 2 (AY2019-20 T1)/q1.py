# Name:
# Email ID:

def compute_product(num_list):
    # Modify the code below.

    total_product = 1
    for nums in num_list:
        if nums%2 == 1:
            total_product *= nums

    return total_product
    