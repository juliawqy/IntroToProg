# Name:
# Email ID:
def extract_names_2(name_list):
    
    pass
    # Write your code here.

    return_list = []
    current_name = ''

    for names in name_list:
        for ch in names:
            if ch.isalpha() == True or ch == ' ':
                current_name += ch
        if current_name.count(' ') != len(current_name):
            return_list.append(current_name)
            current_name = ''
            
    
    if current_name.count(' ') != len(current_name):
        return_list.append(current_name)
        current_name = ''

    return return_list

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, name_list, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: extract_names_2({name_list})')
        print()
        print(f'Expected: {expected_output}')
        result = extract_names_2(name_list)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
    
    run_test_case(1, ['Alex T5an', '^Harry Potter$', 'Squid$$ Game', 'abc','5 -6- 7-8'], ['Alex Tan', 'Harry Potter', 'Squid Game', 'abc'], "<class 'list'>")
    run_test_case(2, ['Alina Star**kov', 'Jessie Mei   Li'], ['Alina Starkov', 'Jessie Mei   Li'], "<class 'list'>")
    run_test_case(3, ['@@ 12'], [], "<class 'list'>")
    run_test_case(4, [], [], "<class 'list'>")
