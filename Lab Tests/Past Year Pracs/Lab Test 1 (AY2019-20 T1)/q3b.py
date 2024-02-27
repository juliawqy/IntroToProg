# Name:
# Email ID:

import q3a

def calculate_entrance_fees_2(m, n):
    
    # These variables are defined for you to use.
    ADULT_TICKET = 75
    CHILD_TICKET = 50
    
    PACKAGE_A = 140 #2 adults
    PACKAGE_B = 110 #1 adult 1 child
    PACKAGE_C = 200 #2 adults 2 children
    
    # Modify the code below.
    if m == n:
        entrance_fee = q3a.calculate_entrance_fees_1(n)
        return entrance_fee

    elif m > n:
        entrance_fee = q3a.calculate_entrance_fees_1(n)
        if (m-n)%2 == 0:
            entrance_fee = entrance_fee + ((m-n)//2)*PACKAGE_A
        else:
            entrance_fee = entrance_fee + ((m-n)//2)*PACKAGE_A + ADULT_TICKET
    
    else:
        if m%2 == 0:
            entrance_fee = (m//2)*PACKAGE_C
        else:
            entrance_fee = (m//2)*PACKAGE_C + PACKAGE_B
        entrance_fee = entrance_fee + (n-m)*CHILD_TICKET
    
    return entrance_fee
