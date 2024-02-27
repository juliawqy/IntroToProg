# Name:
# Email ID:
def extract_names_1(str_name):
    
    pass
    # Write your code here.

    return_list = []
    current_name = ''

    for ch in str_name:
        if ch != '#':
            current_name += ch
        else:
            if current_name != '':
                return_list.append(current_name)
                current_name = ''
    
    if current_name != '': #remember to append the last one!!
        return_list.append(current_name)
        current_name = ''
    
    return return_list

    
# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, str_name, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: extract_names_1("{str_name}")')
        print()
        print(f'Expected: {expected_output}')
        result = extract_names_1(str_name)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
    
    run_test_case(1, 'Alex Tan##xy1 z####abc$#S', ['Alex Tan', 'xy1 z', 'abc$', 'S'], "<class 'list'>")
    run_test_case(2, '#ab c##def#', ['ab c', 'def'], "<class 'list'>")