# Name:
# Email ID:

def calculate_entrance_fees_1(n):

    # These variables are defined for you to use.
    PACKAGE_B = 110
    PACKAGE_C = 200

    # Modify the code below.
    if n%2 == 0:
        entrance_fee = (n//2)*PACKAGE_C
    else:
        entrance_fee = (n//2)*PACKAGE_C + PACKAGE_B
    return entrance_fee
        