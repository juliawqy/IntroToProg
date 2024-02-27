# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

def trim_number(num1, num2):
    # Replace the code below with your implementation.

    str1 = str(num1)
    if int(str1[-1]) > num2 and (num2 >= 1) and (num2 <= 9):
        new_num = str1[:(len(str1)-1)] + str(num2)
        new_num = int(new_num)
        return new_num
    else:
        return num1 

    