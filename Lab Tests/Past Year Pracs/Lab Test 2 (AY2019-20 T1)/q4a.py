# Name:
# Email ID:

def store_family_relations(family_file):
    # Modify the code below.

    all_family_dict = {}

    with open(family_file) as fi:
        for line in fi:
            line = line.rstrip('\n')
            parents = line.split(':')[0]
            father = parents.split(',')[0][1:]
            mother = parents.split(',')[1][:-1]
            parent_list = [father, mother]

            children = line.split(':')[1].split(';')
            children_list = []
            for child_info in children:
                child_info = child_info.split(',')
                child_info_tuple = (child_info[0][1:],child_info[1][:-1])
                children_list.append(child_info_tuple)
            
            for index, parent in enumerate(parent_list):
                for child in children_list:
                    if index == 0:
                        all_family_dict[(parent, child[0])] = 'father'
                    else:
                        all_family_dict[(parent, child[0])] = 'mother'
            
            for child_tuple in children_list:
                for parent in parent_list:
                    if child_tuple[1] == 'F':
                        all_family_dict[(child_tuple[0]), parent] = 'daughter'
                    else:
                        all_family_dict[(child_tuple[0]), parent] = 'son'


    return all_family_dict