# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

def filter_words(filename, end):
    # Replace the code below with your implementation.

    return_list = []

    with open(filename) as fi:
        for line in fi:
            line = line.rstrip('\n').split(' ')
            for words in line:
                if words[-1] == end:
                    return_list.append(words)
            

    return return_list
