# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

def get_n_odd_numbers(filename, n):
    # Replace the code below with your implementation.

    return_list = []

    with open(filename) as fi:
        for line in fi:
            if len(return_list) < n:
                line = line.rstrip('\n')
                line = int(line)
                if line%2 == 1:
                    return_list.append(line)
    
    return return_list
