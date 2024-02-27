# Name:
# Email ID:

def get_longer_words(file_name):
    # Modify the code below.

    return_list = []

    with open(file_name) as fi:
        for line in fi:
            line = line.rstrip('\n')
            len1 = len(line.split('&')[0])
            if len(line.split('&')[0]) >= len(line.split('&')[1]):
                return_list.append(line.split('&')[0])
            else:
                return_list.append(line.split('&')[1])

    return return_list