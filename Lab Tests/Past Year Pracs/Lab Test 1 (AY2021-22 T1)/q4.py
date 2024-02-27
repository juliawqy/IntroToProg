# Name:
# Email ID:

import itertools

def print_puzzle(puzzle):

    print(' |0 1 2 3 4 5 6 7 ')
    print('-' * 17)
    index = 0
    for row in puzzle:
        print(str(index) + '|', end='')
        index = index + 1
        for ch in row:
            print(ch + ' ', end='')
        print()
        
def solve_puzzle(puzzle, word_positions, key, vocabulary):
    # Replace the code below with your implementation.    

    global itertools
    letter_perm = list[itertools.permutations(key)]

    candidate_puzzle = []

    #for perms_index in range(len(letter_perm)):
    for lines in puzzle:
        for ch_line in lines:
            #for ch_num in range(len(letter_perm[perms_index])):
                test_line = ""
                if ch_line != "*":
                    test_line = test_line + ch_line
                #else:
                    #test_line = test_line + letter_perm[perms_index][ch_line]
                candidate_puzzle = candidate_puzzle + [test_line]
    for test_lines in candidate_puzzle:
        word_list = []

        for positions in word_positions: #list of coordinates(puzzle[m], puzzle[m][n]), orientation & length
            if positions[2] == "H":
                is_word = ""
                incom_word = puzzle[(positions[0])][positions[1]:positions[1]+positions[3]]
                for ch_word in incom_word:
                    return candidate_puzzle
                    #for perms in letter_perm: #list of permutations
                        #for ch_perm in perms: #ch in each list of permutation
                            #if ch_word != "*":
                                #is_word = is_word + ch_word
                            #else:
                                #is_word = is_word + ch_perm
                #word_list = word_list + [is_word]
            #elif positions[2] == "V":
                #is_word = ""
                #incom_word = ""
                #for vert_list in range(positions[0],positions[0]+positions[3]):
                    #incom_word = incom_word + puzzle[vert_list][positions[1]]
                #for ch_word in incom_word:
                    #if ch_word != "*":
                        #is_word = is_word + ch_word
                    #else:
                        #is_word = is_word + ch_perm
                #word_list = word_list + [is_word]
        
        #return word_list
    #for test_words in word_list:
        #if test_words != vocabulary:
            #break
        #return word_list

