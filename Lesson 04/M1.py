# Temperature conversion program (celcius-fahrenheit / Fahrenheit-Celcius)

# display program welcome
print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) to convert Fahrenheit to Celsius')
print('Enter (C) to convert Celsius to Fahrenheit')

# Get temperature to convert
which = input('Enter selection: ')

while which != 'F' and which != 'C':
	which = input("Please enter 'F' or 'C': ")
	
temp = int(input('Enter temperature to convert: '))

# determine temperature tconversion needed and display results
if which == 'F':
	while temp < -459.67:
		temp = int(input('That temperature is below absolute zero. Enter a temperature: '))
	converted_temp = format((temp - 32) * 5/9, '.1f')
	print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
else:
	while temp < -273.15:
		temp = int(input('That temperature is below absolute zero. Enter a temperature: '))
	converted_temp = format((9/5 * temp) + 32, '.1f')
	print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')
