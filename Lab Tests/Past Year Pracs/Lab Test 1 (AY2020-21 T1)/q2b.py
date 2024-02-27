# Name:
# Email ID:

def get_max_of_min(list_of_num_tuples): #123, 456
    # Replace the code below with your implementation.
    
    # Note: You’re NOT allowed to use either min()or max()to solve this problem.

    if list_of_num_tuples == []:
        return None

    tuple_min_list = []

    for tuples in list_of_num_tuples: #eg 456
        tuple_min = 10000000000000000000 #
        for tuple_index in range(3): #0 to 2, eg 4
            if tuples[tuple_index] <= tuple_min: #4 < 100000...
                tuple_min = tuples[tuple_index] #1
                tuple_min_list = tuple_min_list + [tuple_min] #1
    
    for elements in tuple_min_list:
        new_max = -10000000000000000000
        if elements >= new_max:
            new_max = elements
    return new_max