# Name:
# Email ID:

def transform(str1, str2): 
    # Modify the code below.

    result_list = [str1] 
    current_str = str1 

    for ch_num in range(len(str2)): 
        index_ch = current_str.find(str2[ch_num]) 
        for k in range(index_ch,ch_num,-1): 
            new_str = current_str[:k-1] + current_str[k] + current_str[k-1] + current_str[k+1:] 
            result_list = result_list + [new_str]
            current_str = new_str






    return result_list
        
    