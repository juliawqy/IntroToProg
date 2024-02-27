# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

def read_courses(filename):
    # Replace the code below with your implementation.

    return_dict = {}

    with open(filename) as fi:
        for line in fi:
            line = line.rstrip('\n').split('|')
            name = line[1]
            if name not in return_dict:
                return_dict[name] = []
            year = int(line[0][0:4])
            term = int(line[0][-1])
            course = line[2]
            credit = int(line[3])
            score = float(line[4])
            return_dict[name].append((course, year, term, credit, score))

    return return_dict
