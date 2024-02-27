import sys


def run_test():
    print('########## TESTING Q2b ##########')
    # Test Cases
    test_cases = [((1005, [5,4,3]), 1004, 0.5),
              ((176, [6,7,5]), 175, 0.5),
              ((571, [5]), 571, 0.5),
              ((8, [8,3,9]), 3, 0.5),
              ((60008, [8,8,2,8,8,8,8,8,8,8]), 60002, 0.5),
              ((75768, [6]), 75766, 0.5)]
    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q2b import trim_number_with_list

        for (input_numbers, expected_result, score) in test_cases:

            list_num_string = ''
            for i in input_numbers[1]:
                list_num_string = list_num_string+", "+str(i)

            print("\nTest Case: (" + str(input_numbers[0]) + ', [' + list_num_string[2:] + "])")

            try:
                result = trim_number_with_list(input_numbers[0], input_numbers[1])

                print('Expected output:', expected_result, ", type of", type(expected_result))
                print('Actual output  :', result, ", type of", type(result))

                if result == expected_result:
                    total_score += score
                    counter += 1
                    print("+" + str(score) + "/" + str(score)
                            + " marks")
                elif result == str(expected_result):
                    total_score += round(score/2, 2)
                    print("Partial mark given as actual output is of the wrong type.")
                    print("+" + str(round(score/2, 2)) + "/" + str(score)
                              + " marks")       
                else:
                    print("+0.0/" + str(score) + " marks")

            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())


    total_score = round(total_score, 2)
    print('\nTotal Marks: ' + str(total_score) + " out of 3.0")

    return (counter, total_score)

run_test()