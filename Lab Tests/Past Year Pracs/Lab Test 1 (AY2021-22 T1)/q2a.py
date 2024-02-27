# Name:
# Email ID:

def get_right_most_even_digit(number):
    # Replace the code below with your implementation.

    str_number = str(number)

    for num in str_number[len(str_number)::-1]:
        if int(num)%2 == 0:
            return num
        else:
            continue
        
        return None
    