# Name:
# Email ID:

def check_diversity(team):
    # Replace the code below with your implementation.

    count = 0
    for people_info in team:
        if people_info[1] == "M":
            count += 1
    if count != 2 and count != 3:
        return False
    
    list_eth = []
    for people_info in team:
        if people_info[2] not in list_eth:
            list_eth = list_eth + [people_info[2]]
    if len(list_eth) < 3:
        return False

    list_rel = [] 
    for people_info in team:
        if people_info[3] == "Freethinker":
            continue
        elif people_info[3] not in list_rel:
            list_rel = list_rel + [people_info[3]]
    if len(list_rel) < 2:
        return False

    return True





    return None