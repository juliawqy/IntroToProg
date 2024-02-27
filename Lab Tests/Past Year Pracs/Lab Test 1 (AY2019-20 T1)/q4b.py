# Name:
# Email ID:

import itertools
import q4a

def get_seating_arrangement(female_list, male_list, must_list, cannot_list): #eg 3f 3m
    # Modify the code below.
    perm_female = list(itertools.permutations(female_list)) #all p of females, ie 6p
    perm_male = list(itertools.permutations(male_list)) #all p of males, ie 6p

    all_arrangements = []
    for num_perms in range(len(perm_female)): #0 to 5, each is a list
        test_list = []
        for num_females in range(len(female_list)): #0 to 2
            test_list = test_list + [perm_female[num_perms][num_females]] + [perm_male[num_perms][num_females]]
        all_arrangements = all_arrangements + [test_list]
    
    for arrangements in range(len(all_arrangements)):
        is_viable = q4a.check_seating_arrangement(all_arrangements[arrangements], must_list, cannot_list)
        if is_viable == True:
            return all_arrangements[arrangements]
        else:
            continue


            
