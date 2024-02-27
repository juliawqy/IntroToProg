# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

import q2a

def trim_number_with_list(num, num_list):
    # Replace the code below with your implementation.
    global q2a

    new_num = num

    for digits in num_list:
        new_num = q2a.trim_number(new_num, digits)
    
    return new_num

