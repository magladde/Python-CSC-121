# Metric conversion program

# program introduction
print('This program takes user input for weight, length short and length long')
print('and converts them from imperial to metric or metric to imperial.')
print()

# get user input for starting unit
system = ''
while system != 'I' and system != 'M':
	system = input("Choose starting units, 'I' for imperial and 'M' for metric: ")

# get weight, short lenght, or long length to convert
to_convert = ''
while to_convert != 'W' and to_convert != 'S' and to_convert != 'L':
	to_convert = input("Choose 'W' for weight conversion, 'S' for short length conversion, and 'L' for long distance conversion: ")

# get amount to convert
if system == 'I':
	if to_convert == 'W':
		pounds = int(input('Enter the number of pounds: '))
		pounds_to_grams = format((pounds * 453.59237), '.1f')
		print(pounds_to_grams, 'grams in', pounds, 'pounds.')
	elif to_convert == 'S':
		inches = int(input('Enter the number of inches: '))
		inches_to_centimeters = format((inches * 2.54), '.1f')
		print(inches_to_centimeters, 'centimeters in', inches, 'inches.')
	else:
		miles = int(input('Enter the number of miles: '))
		miles_to_kilo = format((miles * 1.6), '.1f')
		print(miles_to_kilo, 'kilometers in', miles, 'miles.')
		
else:
	if to_convert == 'W':
		grams = int(input('Enter the number of grams: '))
		grams_to_pounds = format((grams * 0.00220462) , '.1f')
		print(grams_to_pounds, 'pounds in', grams, 'grams.')
	elif to_convert == 'S':
		centimeters = int(input('Enter the number of centimeters: '))
		centimeter_to_inches = format((centimeters * 0.393701), '.1f')
		print(centimeter_to_inches, 'inches in', centimeters, 'centimters.')
	else:
		kilometer = int(input('Enter the number of kilometers: '))
		kilometer_to_mile = format((kilometer * 0.621371), '.1f')
		print(kilometer_to_mile, 'miles in', kilometer, 'kilometers.')
