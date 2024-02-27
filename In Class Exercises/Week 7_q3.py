def print_triangle(ch, num_rows):

    return_list = []

    for i in range(num_rows,-1,-1):
        return_list = return_list + [(num_rows-i)*' ' + ((i*2)-1)*ch + (num_rows-i)*' ']

    for results in return_list[::-1]:
        print(results)

def print_frame(ch, num_rows, num_cols):
    print(ch*num_cols)
    for i in range(num_rows-2):
        print(ch + ' '*(num_cols-2) + ch)
    print(ch*num_cols)


