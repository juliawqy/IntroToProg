import sys

def run_test():
    print('########## TESTING Q1 ##########')
    # Counter is to record how many test cases are passed.
    # Some test cases are given partial marks.
    counter = 0.0
    # Test Cases
    test_cases = [('vegetable', '5%', 1),
                ('vegetables', '5%', 1),
                ('fruits', '7.5%', 1),
                ('flours', '10%', 1),
                ('seasoningssxx', 'No Promotion', 1),
                ('fru', 'No Promotion', 1),
                ('', 'No Promotion', 0.5),
                ('  ', 'No Promotion', 0.5)]
    
    # ##########

    total_score = 0.0

    try:
        from q1 import get_promotion

        for (input_str, expected_result, score) in test_cases:

            print("\nTest Case: '" + input_str + "'")

            try:
                result = get_promotion(input_str)

                print('Expected output:', expected_result)
                print('Actual output  :', result)

                if result == expected_result:
                    counter += 1
                    total_score += score
                    print("+" + str(score) + "/" + str(score)
                            + " marks")
                elif result.lower() == expected_result.lower():
                    total_score += round(score/2, 2)
                    print("Partial mark given. Note that the expected output is case-sentitive.")
                    print("+" + str(round(score/2, 2)) + "/" + str(score)
                              + " marks")

                else:
                    print("+0.0/" + str(score) + " marks")

            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())


    total_score = round(total_score, 2)
    print('\nTotal Marks: ' + str(total_score) + " out of 7.0")
    
    return (counter, total_score)

run_test()