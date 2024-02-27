import sys

def run_test():
    print('########## TESTING Q3a ##########')
    # Test Cases
    test_cases = [('', [], 0.5),
                ('+', ['+'], 0.5),
                ('+-', ['+-', '-+'], 0.25),
                ('abc', ['abc', 'bca', 'cab'], 0.25),
                ('~!@#$', ['~!@#$', '!@#$~', '@#$~!', '#$~!@', '$~!@#'], 0.25),
                ('111', ['111', '111', '111'], 0.25),
                ('987654321', ['987654321', '876543219', '765432198', '654321987', 
                            '543219876', '432198765', '321987654', '219876543', 
                            '198765432'], 0.5)]
    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q3a import shift_string

        for (input_str, expected_result, score) in test_cases:

            print("\nTest Case: '" + input_str + "'")

            try:
                result = shift_string(input_str)

                print('Expected output:', expected_result)
                print('Actual output  :', result)

                if result == expected_result:
                    total_score += score
                    counter += 1
                    print("+" + str(score) + "/" + str(score)
                            + " marks")
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