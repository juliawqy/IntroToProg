import sys

def run_test():
    print('########## TESTING Q2a ##########')
    
    # Test Cases
    test_cases = [((1005, 2), 1002, 1),
              ((171, 7), 171, 1),
              ((571, 1), 571, 1),
              ((100, 5), 100, 0.5),
              ((6, 2), 2, 0.5),
              ((60008, 2), 60002, 0.5),
              ((75768, 9), 75768, 0.5)]
    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q2a import trim_number

        for (input_numbers, expected_result, score) in test_cases:

            print("\nTest Case: (" + str(input_numbers[0]) + ', ' + str(input_numbers[1]) + ")")

            try:
                result = trim_number(input_numbers[0], input_numbers[1])

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
    print('\nTotal Marks: ' + str(total_score) + " out of 5.0")

    return (counter, total_score)

run_test()