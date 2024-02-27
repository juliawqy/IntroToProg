# Name:
# Email ID:

from q4b import find_words

def find_all_words(word_list, input_str, step):
    # Replace the code below with your implementation.
    return_list = []
    return_dict = {}

    global find_words

    for word in word_list:
        if word not in return_dict.keys():
            return_dict[word] = []
            return_dict[word].extend(find_words([word], input_str, step))
        if return_dict[word] != []:
            for first_match in return_dict[word]:
                current_list = []
                for i in range(len(word)):
                    current_list.append(0)
                print(len(current_list))
                print(len(word))
                while len(current_list) == len(word):
                    current_list = []
                    for index in range(len(first_match)-1,-1,-1):
                        if index != len(input_str):
                            check_str = input_str[first_match[index]+1:]
                        else:
                            check_str = ''
                        new_num = find_words([input_str [first_match[index]]], check_str,step)
                        current_list.append(first_match[:index])
                        current_list.append(new_num)
                        if index != len(first_match) -1:
                            current_list.append(first_match[index+1:])
                    if len(current_list) == len(word):
                        return_dict[word].extend(current_list)




    for keys in return_dict.keys():
        return_list.extend(return_dict[keys])
    print(return_dict)
    

                        

    return return_list