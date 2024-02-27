import week2_utility

age = int(input("What's your age? "))
gender = input("What's your gender [M|F]? ")
premium = week2_utility.get_insurance_premium(age, gender)
print("Your premium is $" + str(premium))
