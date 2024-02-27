def transform_string(string):

    digits = '0123456789'
    small_letters = 'abcdefghijklmnopqrstuvwxyz'
    upper_letters = small_letters.upper()
    end_str = ''
    upper_count = 0
    lower_count = 0
    digit_count = 0
    sym_count = 0 

    for ch in string:
        if ch in digits:
            end_str = end_str + 'd'
            digit_count += 1
        elif ch in upper_letters:
            end_str = end_str + 'L'
            upper_count += 1
        elif ch in small_letters:
            end_str = end_str + 'l'
            lower_count += 1
        else:
            end_str = end_str + 's'
            sym_count += 1

    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")
    print(f"Number of digits: {digit_count}")
    print(f"Number of symbols: {sym_count}")
    print()
    print(f"The transformed text is: {end_str}")

    return end_str
