# This program takes user input which indicates the number of cities
# that a traveling salesman needs to travel to. The program takes the 
# number of cities required to travel to and calculates the amount of 
# time needed to calculate the answer using brute force approach. This
# program assumes that a computer can calculate the lengths of one 
# million routes per second and gives the brute-froce approach time
# in years.

import math

# display program welcome
print('Welcome to the traveling salesman brute-force calculator!')
print('Input an integer for the number of cities that a traveling ' +
	'salesman would need to calculate.')
print('Answer is displayed in years to calculate at a rate of ' + 
	'one million routes per second.')

# get user input
number_of_cities = int(input('How many cities?: '))

# calculate result
number_of_routes = math.factorial(number_of_cities)
time_to_calculate = (number_of_routes / 1000000) / (31536000)

# display result
print()
print('It would take', time_to_calculate, 'years to brute-force calculate', 
	'the traveling salesman problem with', number_of_cities, 'cities.')
