# Name:
# Email ID:
    
def get_persons(person_list, n):
    pass
    # Write your code here.

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, person_list, n, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_persons("{person_list}", {n})')
        print()
        print(f'Expected (in any order): {expected_output}')
        result = get_persons(person_list, n)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        
    person_list = [('john', 'M'), ('alex', 'F'), ('don', 'M'), ('val', 'F'), ('ann', 'F')]
    expected_list = [('don', 'M'), ('john', 'M'), ('alex', 'F')]
    run_test_case(1, person_list, 2, expected_list, "<class 'list'>")

    person_list = [('john', 'M'), ('alex', 'F'), ('don', 'M'), ('val', 'F'), ('ann', 'F')]
    expected_list = [('john', 'M'), ('don', 'M')]
    run_test_case(2, person_list, 3, expected_list, "<class 'list'>")

    person_list = [('a', 'M'), ('b', 'F'), ('c', 'M'), ('d', 'M'), ('e', 'M'), ('f', 'M'), ('g', 'M'), ('h', 'M')]
    expected_list = [('b', 'F')]
    run_test_case(3, person_list, 7, expected_list, "<class 'list'>")

    person_list = [('a', 'M'), ('b', 'F'), ('c', 'M'), ('d', 'M'), ('e', 'M'), ('f', 'M'), ('g', 'M'), ('h', 'M')]
    expected_list = []
    run_test_case(4, person_list, 8, expected_list, "<class 'list'>")
    

