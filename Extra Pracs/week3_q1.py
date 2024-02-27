def count_down(n):
    print(n)
    if n > 1:
        count_down(n - 1)

def compute_factorial(n):

    if n == 1:
        return 1
    else:
        return (n*compute_factorial(n-1))

def get_num_digits(n):

    count = 1
    current_num = n
    if current_num//10 > 0:
        return (count + get_num_digits(n//10))
    else:
        return (count)


def display_fibonacci_numbers(n): #undone

    if n > 1:
        if n <= 1:
            return n
        else:
            return (display_fibonacci_numbers(n-1) + display_fibonacci_numbers(n-2))
    elif n == 1:
        print(1, end=' ')
        return n+1
    else:
        print(n, end=' ')
        return n

display_fibonacci_numbers(4)
    