# This program calculates the total number of routes possible for the
# traveling salesman problem. This is calculating the factorial of the 
# number of cities entered by the user.

number_of_cities = int(input('How many cities? '))
import math
possible_routes= math.factorial(number_of_cities)
print('For', number_of_cities, ', there are', possible_routes, 'possible routes.')

