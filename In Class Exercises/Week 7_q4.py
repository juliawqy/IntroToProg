def is_pangram(sentence):

    letters = 'abcdefghijklmnopqrstuvwxyz'
    new_sentence = sentence.lower()

    for ch in letters:
        if ch in sentence:
            continue
        else:
            return False
    return True