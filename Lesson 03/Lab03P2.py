# Calculate Time Program

# program greeting
print('Hello, this program calculates what time it is based off of the')
print('number of seconds past midnight. This program takes user input')
print('in the form of number of seconds past midnight.')

# get user input for number of seconds past midnight
num_seconds = int(input('\nEnter number of seconds since midnight: '))

# calculate the current time
hour = num_seconds // 3600
minute = (num_seconds - (hour * 3600)) // 60
seconds = (num_seconds - (hour * 3600) - (minute * 60))

if num_seconds >= 43200:
	meridiem = 'PM'
	
else:
	meridiem = 'AM'

# print the time
if hour == 0:
	hour = 12

elif hour > 12:
	hour = hour - 12
print('The time is', hour, ':', minute, ':', seconds, meridiem)
