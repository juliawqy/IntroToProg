# Name:
# Email ID:

def get_number_of_long_strings(str_list, n):
    # Modify the code below.
    is_longer = 0
    for num in range(len(str_list)):
        if len(str_list[num]) > n:
            is_longer = is_longer + 1
  
    return is_longer
