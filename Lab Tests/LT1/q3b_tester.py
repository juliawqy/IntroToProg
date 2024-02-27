import sys
    
def run_test():
    print('########## TESTING Q3b ##########')
    # Test Cases

    # Test Case 1: empty string
    tc1_in = ('', [], [])
    tc1_out = ''
    tc1_s = 0.25

    # Test Case 2: len_list has a single element
    tc2_in = ('CAT', [3], [])
    tc2_out = 'CAT'
    tc2_s = 0.25

    # Test Case 3: len_list has two elements
    tc3_in = ('MOUSE', [2, 3], ['-'])
    tc3_out = 'MO-USE'
    tc3_s = 0.5

    # Test Case 4: len_list has more than two elements
    tc4_in = ('elephant', [3, 1, 4], ['()', '[]'])
    tc4_out = 'ele()p[]hant'
    tc4_s = 0.5

    # Test Case 5: input string as some spaces
    tc5_in = (' new york ', [2, 5, 2, 1], ['$', '#', '@'])
    tc5_out = ' n$ew yo#rk@ '
    tc5_s = 0.5

    # Test Case 6: empty string in connector list
    tc6_in = ('singapore', [3, 3, 3], ['', 'asia'])
    tc6_out = 'singapasiaore'
    tc6_s = 0.25

    # Test Case 7: a combination of different scenarios
    tc7_in = ('This is a long test.', [1, 2, 3, 4, 5, 5], [' ', '123', '**', '', '@ @'])
    tc7_out = 'T hi123s i**s a long @ @test.'
    tc7_s = 0.25

    test_cases = [(tc1_in, tc1_out, tc1_s), 
                (tc2_in, tc2_out, tc2_s),
                (tc3_in, tc3_out, tc3_s),
                (tc4_in, tc4_out, tc4_s),
                (tc5_in, tc5_out, tc5_s),
                (tc6_in, tc6_out, tc6_s),
                (tc7_in, tc7_out, tc7_s)]
    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q3b import construct_string
        
        for (input_tuple, expected_result, score) in test_cases:

            print('\nTest Case:', input_tuple)
            

            orig_str = input_tuple[0]
            len_list = input_tuple[1]
            cnct_list = input_tuple[2]

            try:
                result = construct_string(orig_str, len_list, cnct_list)

                print("Expected output: '" + expected_result + "'")
                if isinstance(result, str):
                    print("Actual output  : '" + result + "'")
                else:
                    print("Actual output  : " + str(result))

                if result == expected_result:
                    total_score += score
                    counter += 1
                    print("+" + str(score) + "/" + str(score) + " marks")
                else:
                    # give some partial marks if the output string misses 
                    # only the last segment
                    if orig_str != '':
                        len_last_seg = len_list[-1]
                        mod_expected_result = expected_result[0:len(expected_result)-len_last_seg]
                        if result == mod_expected_result:
                            print('Output is partially correct')
                            total_score += score / 2
                            print("+" + str(score/2) 
                                    + "/" + str(score) + " marks")
                        else:
                            print("+0.0/" + str(score) + " marks")
                    else:
                        print("+0.0/" + str(score) + " marks")

            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())
    
    total_score = round(total_score, 2)
    print('\nTotal Marks: ' + str(total_score) + " out of 2.5")
   
    return (counter, total_score)

run_test()