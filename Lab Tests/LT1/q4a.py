# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

def is_overlapping(rect_1, rect_2):
    # Replace the code below with your implementation.
    
    if rect_1[1] <= rect_2[1]:
        left_rect = rect_1
        right_rect = rect_2
    else:
        left_rect = rect_2
        right_rect = rect_1
    
    if rect_1[2] >= rect_2[2]:
        up_rect = rect_1
        down_rect = rect_2
    else:
        up_rect = rect_2
        down_rect = rect_1
    
    wid_left_rect = left_rect[1] + left_rect[3]
    hht_down_rect = down_rect[2] + down_rect[4]

    if wid_left_rect > right_rect[1] and hht_down_rect > up_rect[2]:
        return True
    else:
        return False

