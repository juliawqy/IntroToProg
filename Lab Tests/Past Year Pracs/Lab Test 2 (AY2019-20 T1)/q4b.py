# Name:
# Email ID:


def get_relation_through_link(family_dict, link):
    # Modify the code below.

    relations = []
    relation_dict = {}

    with open('relation_mapping.txt') as fi:
        for line in fi:
            line = line.rstrip('\n')
            key, value = line.split(':')
            relation_dict[key] = value

    for index, name in enumerate(link[:-1]):
        relations.append(family_dict[(name, link[index+1])])

    while len(relations) > 2:
        relations = [relation_dict[str(f'({relations[0]},{relations[1]})')]] + relations[2:]


    return relation_dict[str(f'({relations[0]},{relations[1]})')]
    