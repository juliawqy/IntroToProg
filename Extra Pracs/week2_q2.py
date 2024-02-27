print('abc' * 5)
print('%' * 10)
print('a' * 0)
print('b' * (-2))

print('12345\n12345')

def print_square(symbol, size):
    print(symbol*size)
    space = " "
    for i in range((size-2)):
        print(f"{symbol}{space*(size - 2)}{symbol}")
    print(symbol*size)

print_square("*", 5)
print_square("1", 10)
print_square("^", 1)