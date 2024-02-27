# Name:
# Email ID:

def check_sum(n1, n2, n3):
    # Modify the code below.
    has_sum = False
    if (n1 == n2 + n3) or (n2 == n1 + n3) or (n3 == n1 + n2):
        has_sum = True
    return has_sum
    