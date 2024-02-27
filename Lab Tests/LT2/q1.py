# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

def check_record(record):
    # Replace the code below with your implementation.

    return_value = False

    if type(record[0]) == str:
        if type(record[1]) == int:
            if type(record[2]) == int:
                if record[1] == len(record[0]):
                    if record[2] > record[1]:
                        return_value = True

    return return_value
