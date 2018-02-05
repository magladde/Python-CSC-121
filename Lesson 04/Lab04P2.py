# This program calculates the number of seconds since midnight

# program introduction
print('Hello, this program calculates the number of seconds since ')
print('midnight. You will be asked to enter 4 pieces of information: ,')
print('hour, minute, second, and AM/PM.')

# get user input for hour, minute, second, and AM/PM
hour = int(input('\nEnter hour: '))
while hour not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
	print('Hour must be from 1 to 12.')
	hour = int(input('Enter hour: '))
	
minute = int(input('Enter minute: '))
while minute not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, + \
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, + \
32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, + \
49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59): 
	print('Minute must be from 0 to 59.')
	minute = int(input('Enter minute: '))
	
second = int(input('Enter second: '))
while second not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, + \
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, + \
32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, + \
49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59):
	print('Second must be from 0 to 59.')
	second = int(input('Enter second: '))
	
meridiem = input('Enter AM or PM: ')
meridiem = meridiem.lower()
while meridiem not in ('am', 'pm'):
	print('Please enter AM or PM.')
	meridiem = input('Enter AM or PM: ')
	meridiem = meridiem.lower()

# calculate seconds since midnight
if meridiem == 'pm' and hour == 12:
	hour = 12
	
elif meridiem == 'am' and hour == 12:
	hour = 0
	
elif meridiem == 'pm':
	hour = hour + 12
	
total_seconds = (hour * 3600) + (minute * 60) + second

# display output
print('Seconds since midnight: ', total_seconds)
