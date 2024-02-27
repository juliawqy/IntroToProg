# Name:
# Email ID:

def get_sum_of_digits(my_str):
    # Replace the code below with your implementation.
    
    digits = '0123456789'
    sum = 0

    for ch in my_str:
        if digits.find(ch) == -1:
            continue
        else:
            sum = sum + int(ch)

    return sum