# This program calculates the number of seconds since midnight

# program introduction
print('Hello, this program calculates the number of seconds since ')
print('midnight. You will be asked to enter 4 pieces of information: ,')
print('hour, minute, second, and AM/PM.')

# get user input for hour, minute, second, and AM/PM
hour = int(input('\nEnter hour: '))
minute = int(input('Enter minute: '))
second = int(input('Enter second: '))
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
