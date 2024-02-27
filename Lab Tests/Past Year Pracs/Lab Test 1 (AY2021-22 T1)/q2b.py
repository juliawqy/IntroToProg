# Name:
# Email ID:

def get_all_third_digits(str_list):
    # Replace the code below with your implementation.

    digits_list = []
    digits = "0123456789"
    count = 0
    
    for strings in str_list:
        for ch in strings:
            if digits.find(ch) != -1:
                count += 1
                if count == 3:
                    digits_list = digits_list + [int(ch)]
                    break
        count = 0

    return digits_list
