# Name:
# Email ID:

from q4b import get_relation_through_link

def get_relation(family_dict, p1, p2):
    # Modify the code below.

    global get_relation_through_link

    link = []

    for key in family_dict.keys():
        if key[0] not in link:
            link.append(key[0])
    
    if link.index(p1) < link.index(p2):
        link = link[link.index(p1):link.index(p2)+1]
    else:
        link = link[::-1]
        link = link[link.index(p1):link.index(p2)+1]     
    
    return_relation = get_relation_through_link(family_dict, link)

    return return_relation