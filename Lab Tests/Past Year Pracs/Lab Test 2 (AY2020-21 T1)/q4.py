# Name:
# Email ID:
def get_daily_spending(filename, start_day, end_day, month, year):
    # Write your code here.

    import os

    if os.path.isfile(filename) == False: #bruh wtf
        return [0]

    daily_spent = {}

    for num in range(start_day,end_day+1):
        daily_spent[num] = 0

    with open(filename) as fi:
        for line in fi:
            line = line.rstrip('\n')
            date = line.split('|')[0].split('/') #list of day, mth, year as str
            amt = int(line.split('|')[1])
            if int(date[0]) >= start_day and int(date[0]) <= end_day:
                if int(date[1]) == month:
                    if int(date[2]) == year:
                        daily_spent[int(date[0])] += amt


    return list(daily_spent.values())

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    n = 0

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('trans_file.txt', 3, 5, 10, 2020)")
    result = get_daily_spending('trans_file.txt', 3, 5, 10, 2020)
    print("Expected : [13500, 31520, 100]")
    print(f"Actual   : {result}")
    print()

    print("Expected return type : <class 'list'>")
    print(f"Actual return type   : {type(result)}")    
    
    print()
    
    print("Expected return type of the first element of the list : <class 'int'>")
    print("Actual return type of the first element of the list   : ", end="")
    if (isinstance(result, list)):
        print(type(result[0]))
    else:
        print("N/A")

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('trans_file.txt', 6, 7, 10, 2020)")
    result = get_daily_spending('trans_file.txt', 6, 7, 10, 2020)
    print("Expected : [0, 0]")
    print(f"Actual   : {result}")
    print()

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('trans_file.txt', 2, 6, 10, 2020)")
    result = get_daily_spending('trans_file.txt', 2, 6, 10, 2020)
    print("Expected : [0, 13500, 31520, 100, 0]")
    print(f"Actual   : {result}")
    print()

    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('spending_file.txt', 1, 2, 1, 2020)")
    result = get_daily_spending('spending_file.txt', 1, 2, 1, 2020)
    print("Expected : [1200, 0]")
    print(f"Actual   : {result}")
    print()
    
    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('spending_file.txt', 1, 10, 2, 2020)")
    result = get_daily_spending('spending_file.txt', 1, 10, 2, 2020)
    print("Expected : [50, 0, 0, 0, 0, 0, 0, 0, 0, 80]")
    print(f"Actual   : {result}")
    print()
    
    
    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('empty.txt', 2, 6, 10, 2020)")
    result = get_daily_spending('empty.txt', 2, 6, 10, 2020)
    print("Expected : [0, 0, 0, 0, 0]")
    print(f"Actual   : {result}")
    print()

    
    n += 1
    print('-' * 40)
    
    print(f"Test {n} : get_daily_spending('empty.txt', 2, 2, 11, 2020)")
    result = get_daily_spending('empty.txt', 2, 2, 11, 2020)
    print("Expected : [0]")
    print(f"Actual   : {result}")
    print()