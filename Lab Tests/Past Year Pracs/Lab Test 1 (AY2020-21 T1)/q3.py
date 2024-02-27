# Name:
# Email ID:

def check_math(list_of_equations):
    # Replace the code below with your implementation.

    operants = ["+", "-", "*", "//", "%"]

    if list_of_equations == []:
        is_correct = True

    for equations in list_of_equations:
        for operators in operants:
            if equations.find(operators) != -1:
                eqn_part_1 = equations.split(operators)
                first_int = int(eqn_part_1[0])
                eqn_parts_2_and_3 = eqn_part_1[1].split("=")
                second_int = int(eqn_parts_2_and_3[0])
                last_int = int(eqn_parts_2_and_3[1])
                if operators == "+":
                    new_eqn = first_int + second_int
                elif operators == "-":
                    new_eqn = first_int - second_int
                elif operators == "*":
                    new_eqn = first_int * second_int
                elif operators == "//":
                    new_eqn = first_int // second_int
                else:
                    new_eqn = first_int % second_int                
                
                if new_eqn == last_int:
                    is_correct = True
                else:
                    is_correct = False
                    return is_correct
            
            else:
                continue

    return is_correct