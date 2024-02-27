# Name:
# Email ID:
def get_polynomial(poly_str):

    # Write your code here.

    poly_dict = {}
    poly_str = poly_str.replace(' ', '')
    operators = '-+'
    poly_list = poly_str.split('x')
    current_coefficient = ''

    for piece_index, pieces in enumerate(poly_list[1:]):
        if pieces[0] == '^':
            current_degree = ''
            for ch in pieces:
                if ch == '^':
                    continue
                elif ch not in operators:
                    current_degree += ch
                else:
                    if current_degree not in poly_dict:
                        poly_dict[int(current_degree)] = 0
                    for ch_bfr in poly_list[piece_index-1][-1::-1]:
                        if ch_bfr.isnumeric() == True:
                            current_coefficient = ch_bfr + current_coefficient
                        elif ch_bfr in operators:
                            current_coefficient += ch_bfr + current_coefficient
                            break
                    poly_dict[int(current_degree)] += int(current_coefficient)
                    current_coefficient = 0
                    break     
        elif pieces.count('-') + pieces.count('+') >= 2:
            if 0 not in poly_dict:
                poly_dict[0] = 0
        else:
            if 1 not in poly_dict:
                poly_dict[1] = 0


    return poly_dict

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0
    
    tc_num += 1
    print('-' * 40)
    
    poly_str = '2x - 2x^2 + 3x - 1 + 6x^3'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print("Expected : [6, -2, 5, -1]")
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print() 

    print("Expected return type : <class 'list'>")
    print(f"Actual return type   : {type(result)}")    
    
    print()
    
    print("Expected return type of the first element of the list : <class 'int'>")
    print("Actual return type of the first element of the list   : ", end="")
    if (isinstance(result, list)):
        print(type(result[0]))
    else:
        print("N/A")    

    tc_num += 1
    print('-' * 40)
    
    poly_str = '  4x -2x^2 +   3x^5 -   6x^2'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print('Expected : [3, 0, 0, -8, 4, 0]')
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print()  

    tc_num += 1
    print('-' * 40)
    
    poly_str = '3x^2 - 2x - 3x^2'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print('Expected : [-2, 0]')
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print()      

