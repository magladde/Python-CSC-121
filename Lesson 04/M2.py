# Temperature conversion program (celcius-fahrenheit / Fahrenheit-Celcius)

# display program welcome
print('This program will convert temperatures (Fahrenheit/Celsius)')
print('Enter (F) if starting temperature is Fahrenheit')
print('Enter (C) if starting temperature is Celsius')
print('Enter (K) if starting temperature is Kelvin')

# Get temperature to convert
which = input('Enter selection starting temperature scale: ')
while which != 'F' and which != 'C' and which != 'K':
	which = input("Please enter 'F', 'C', or 'K': ")
	
convert_scale = input('Enter desired temperature scale: ')
while convert_scale != 'F' and convert_scale != 'C' and convert_scale != 'K':
	convert_scale = input("Please enter 'F', 'C', or 'K': ")
	
temp = int(input('Enter temperature to convert: '))

# determine temperature tconversion needed and display results
if which == 'F':
	while temp < -459.67:
		temp = int(input('That temperature is below absolute zero. Enter a temperature: '))
	if convert_scale == 'C':
		converted_temp = format((temp - 32) * 5/9, '.1f')
		print(temp, 'degrees Fahrenheit equals', converted_temp, 'degrees Celsius')
	else:
		converted_temp = (temp - 32) * 5/9
		kelvin_temp = format((converted_temp + 273.15), '.1f')
		print(temp, 'degrees Fahrenheit equals', kelvin_temp, 'degrees Kelvin')
elif which == 'C':
	while temp < -273.15:
		temp = int(input('That temperature is below absolute zero. Enter a temperature: '))
	if convert_scale == 'F':
		converted_temp = format((9/5 * temp) + 32, '.1f')
		print(temp, 'degrees Celsius equals', converted_temp, 'degrees Fahrenheit')
	else:
		converted_temp = format((temp + 273.15), '.1f')
		print(temp, 'degrees Celsius equals', converted_temp, 'degress Kelvin')
else:
	while temp < 0:
		temp = int(input('That temperature is below absolute zero. Enter a temperature: '))
	if convert_scale == 'F':
		converted_temp_celsius = temp - 273.15
		converted_temp_fahrenheit = format((converted_temp_celsius * 9/5) + 32, '.1f')
		print(temp, 'degrees Kelvin equals', converted_temp_fahrenheit, 'degrees Fahrenheit')
	else:
		converted_temp_celsius = format(temp - 273.15, '.1f')
		print(temp, 'degrees Kelvin equals', converted_temp_celsius, 'degrees Celsius')
		
