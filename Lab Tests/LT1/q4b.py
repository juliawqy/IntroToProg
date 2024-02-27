# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

import q4a

def find_overlapping_pairs(rect_list):
    # Replace the code below with your implementation.

    global q4a

    overlap_rects = []

    for rect_index in range(len(rect_list)):
        for compare_rect_index in range(rect_index+1,len(rect_list)):
            if q4a.is_overlapping(rect_list[rect_index],rect_list[compare_rect_index]) == True:
                overlap_rects = overlap_rects + [(rect_list[rect_index][0], rect_list[compare_rect_index][0])]
    
    return overlap_rects



