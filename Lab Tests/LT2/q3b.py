# Name: Wong Qian Yu
# Email ID: qianyu.wong.2022

from q3a import read_courses

def calculate_student_gpa(filename, start_term, end_term):
    # Replace the code below with your implementation.

    return_dict = {}
    course_info_dict = read_courses(filename)
    
    for name in course_info_dict.keys():
        total_score = 0
        num_course = 0
        total_credits = 0
        for info in course_info_dict[name]:
            if (info[1] > start_term[0] and info[1] < end_term[0]) or (info[1] == start_term[0] and info[2] >= start_term[1]) or (info[1] == end_term[0] and info[2] <= end_term[1]): 
            #split into 3 scenarios to compare, if above and below start and end year, if = start year or = end year then compare term for last 2 scenarios
                total_score += info[3]*info[4]
                num_course += 1
                total_credits += info[3]
        return_dict[name] = (num_course, round((total_score/total_credits), 1))

    return return_dict

