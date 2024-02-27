# Name:
# Email ID:

def add_even_numbers(str_list):
    # Modify the code below.
    even_sum = 0
    for n in range(len(str_list)):
        sub_list = str_list[n].split("|")
        for num in sub_list:
            if int(num)%2 == 0:
                even_sum = even_sum + int(num)
    return even_sum

