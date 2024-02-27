# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

def find_words(word_list, input_str, step):
    # Replace the code below with your implementation.

    return_list = []

    for word in word_list:
        current_list = []
        count = 0
        for ch_word in word:
            if ch_word in input_str[count:]:
                current_list.append(input_str[count:].index(ch_word)+count)
                count = input_str[count:].index(ch_word)+count+step
        if len(current_list) == len(word):
            return_list.append(current_list)
        else:
            return_list.append([])

    return return_list