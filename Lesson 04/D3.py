# The first-time home buyer tax credit program

# program introduction
print('This program determines if an individual qualifies for a')
print('government First-Time Home Buyer Tax Credit of $8,000.')
print('Individuals are available to those that (a) bought a house')
print('that cost less than $800,000, (b) had a combined income of')
print('under $225,000 and (c) had not owned a primary residence in the')
print('last three years.')
print()

# get user input for cost_of_home, combined_income, and previous 
# ownership
cost_of_home = int(input('Enter the value of the home: '))
combined_income = int(input('Enter the combined income of individuals purchasing home: '))
previous_ownership_flag = False
previous_ownership = input('Enter [y/n] if you have previously owned a home in the past three years: ')
while previous_ownership != 'y' and previous_ownership != 'n':
	previous_ownership = input('Enter[y/n] if you have previously owned a home in the past three years: ')
if previous_ownership == 'y':
	previous_ownership_flag = True

if previous_ownership_flag == True or cost_of_home > 799999 or combined_income >22499:
	print('You are not qualified for First-Time Home Buyer Tax Credit.')
else:
	print('You are qualified for First-Time Home Buyer Tax Credit.')
