# Name:
# Email ID:

def check_seating_arrangement(arrangement, must_list, cannot_list):
    # Modify the code below.

    for num_must in range(len(must_list)):
        person_want = must_list[num_must][0]
        num_index = arrangement.index(must_list[num_must][0])
        person_left = arrangement[num_index-1]
        if num_index == len(arrangement)-1:
            person_right = arrangement[0]
        else:
            person_right = arrangement[num_index+1]
        if person_left == must_list[num_must][1] or person_right == must_list[num_must][1]:
            must_fulfilled = True
        else:
            must_fulfilled = False
            break
    if must_list == []:
        must_fulfilled = True

    for num_cannot in range(len(cannot_list)):
        person_want = cannot_list[num_cannot][0]
        num_index = arrangement.index(cannot_list[num_cannot][0])
        person_left = arrangement[num_index-1]
        if num_index == len(arrangement)-1:
            person_right = arrangement[0]
        else:
            person_right = arrangement[num_index+1]
        if person_left == cannot_list[num_cannot][1] or person_right == cannot_list[num_cannot][1]:
            cannot_fulfilled = False
            break
        else:
            cannot_fulfilled = True
    if cannot_list == []:
        cannot_fulfilled = True
    
    overall_fulfilled = must_fulfilled and cannot_fulfilled
    return overall_fulfilled

                

        
 