# Name:
# Email ID:

def get_area_difference(width1, length1, width2, length2):
    # Replace the code below with your implementation.

    area_1 = width1*length1
    area_2 = width2*length2

    if area_1 > area_2:
        return area_1 - area_2
    elif area_2 > area_1:
        return area_2 - area_1
    else:
        return 0
