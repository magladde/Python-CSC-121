# This program calculates how many years it would take for all 
# possible chess games to be played if everyone in the world played one 
# unique chess game a day. The assumptions used in this program are
# a world population of 7 billion and 10 raised to the power of 120
# possible chess games that can be played.

import math

# display program welcome
print('Hello, welcome to the chess calculator!')
print('This program calculates how many years it would take play',
	'every unique game of chess ever.')
	
# calculate result
number_of_unique_games = 10 ** 120
world_population = 7 * (10 ** 9)
number_of_years = number_of_unique_games / world_population / 365

# display result
print('It would take', number_of_years, 'years to play every unique',
	'chess game at a rate of ', world_population, 'games a day.')

