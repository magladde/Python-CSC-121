# Leap Years to come

import datetime

# program introduction
print('This program will take user input in the form of a year entered')
print('by the user. This program will then calculate the first occuring')
print('leap year from the current year, until the final year entered')
print('by the user.')
print()

# get current year
current_year= datetime.date.today().year

# get user input for final year
final_year = int(input('Enter final year: '))
while final_year < current_year:
	print('The year you entered is before the current year.')
	final_year = int(input('Enter final year: '))

# generate list of years
num_years = list(range(current_year, (final_year + 1)))

# cycle through the list of years and check to see if each year is a 
# leap year, if leap year place into new list leap_years
leap_years = []
for year in num_years:
	if (year % 4 == 0) and (not(year % 100 == 0) or (year % 400 == 0)):
		leap_years.append(year)
	
# display the leap years
print('The following are the leap years between', current_year, 'and', final_year)
for year in leap_years:
	print(year, end = ',')
