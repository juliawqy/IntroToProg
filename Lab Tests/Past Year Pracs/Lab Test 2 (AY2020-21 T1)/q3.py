# Name:
# Email ID:    
def calculate_term_gpa(term_grades, mapping):
    
    # Write your code here.
    grades_list = []
    total_score = 0

    for index, grade in enumerate(term_grades[:-1]):
        if grade.isalpha() == True:
            if term_grades[index+1].isalpha() == False:
                grades_list.append(term_grades[index:index+2])
            else:
                grades_list.append(grade)
    if term_grades[-1].isalpha() == True:
        grades_list.append(term_grades[-1])
    
    for grades in grades_list:
        total_score += mapping[grades]
    
    final_gpa = total_score/len(grades_list)

    return final_gpa

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)
    
    print(f"Test {tc_num} : calculate_term_gpa('ACAC', {{'A':4, 'B':3, 'C':2, 'F':0}})")
    result = calculate_term_gpa('ACAC', {'A': 4, 'B': 3, 'C': 2, 'F': 0})
    print("Expected : 3.0")
    print(f"Actual   : {result}")
    print()

    print("Expected return type : <class 'float'>")
    print(f"Actual return type   : {type(result)}")  

    tc_num += 1
    print('-' * 40)
    
    print(f'''Test {tc_num}: calculate_term_gpa('A+AA-',
            {{'A+':4.3, 'A':4, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7,
            "'C+':2.3,'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'F':0}})''')
    result = calculate_term_gpa('A+AA-',
                                {'A+': 4.3, 'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                                 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0})
    print("Expected:4.0")
    print(f"Actual  :{result}")
    print()

    tc_num += 1
    print('-' * 40)
    
    print(f"Test {tc_num}:calculate_term_gpa('A*AA',{{'A*':4, 'A':3.5, 'B*':3, 'B':2.5, 'C':2, 'F':0}})")
    result = calculate_term_gpa('A*AA',
                                {'A*': 4, 'A': 3.5, 'B*': 3, 'B': 2.5, 'C': 2, 'F': 0})
    print("Expected:3.6666666666666665")
    print(f"Actual  :{result}")
    print()
