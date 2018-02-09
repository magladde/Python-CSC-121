# number of days in month program

# program greeting
print('This program will display the number of days in a given month.')

# get user input
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month = int(input('Enter the month (1-12): '))
while month not in months:
	month = int(input('That is not a valid month. Please enter the month (1-12): '))

# determine the num of days in month

# februrary
if month == 2:
	year = int(input('Please enter the year (e.g., 2010): '))
	
	if (year % 4 == 0) and (not (year % 100 == 0) or (year % 400 == 0)):
		num_days = 29
	else:
		num_days = 28
		
# january, march, may, july, august, october, december
elif month in (1, 3, 5, 7, 8, 10, 12):
	num_days = 31
	
# april, june, september, november
elif month in (4, 6, 9, 11):
	num_days = 30

# output result
print('There are', num_days, 'days in the month')
