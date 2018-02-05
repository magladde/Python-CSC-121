# Temperature Conversion Program (Celcius to Fahrenheit)

# This program will convert a temperature entered in Celcius to the
# equivalent degrees is Fahrenheit.

# program greeting
print('This program will convert degrees Celciusto degrees Fahrenheit.')

# get temperature in Celcius
celsius = float(input('Enter degrees Celcius: '))

# calc degrees Fahreheit
fahren = (celsius * 9 / 5) + 32

# output degrees Fahrenheit
print(celsius, 'degrees Celcius equals', format(celsius, '.1f'), 'degrees Cesius.')
