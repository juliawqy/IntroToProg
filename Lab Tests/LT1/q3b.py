# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

from hmac import new


def construct_string(orig_str, len_list, cnct_list):
    # Replace the code below with your implementation.

    new_str = orig_str
    return_str = ''

    for str_len_index in range(len(len_list)):
        cut_part = new_str[:len_list[str_len_index]]
        new_str = new_str[len_list[str_len_index]:]
        if str_len_index != (len(len_list)-1):
            return_str = return_str + cut_part + cnct_list[str_len_index]
        else:
            return_str = return_str + cut_part
    
    return return_str

