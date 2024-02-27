# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

def shift_string(orig_str):
    # Replace the code below with your implementation.

    result_list = []
    new_str = ''

    for num_iterations in range(len(orig_str)):
        new_str = orig_str[num_iterations:] + orig_str[:num_iterations]
        result_list = result_list + [new_str]
    
    return result_list

