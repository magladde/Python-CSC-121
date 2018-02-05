# This program is the execution of the Drake equation.
# N = R * p * n * f * i * c * L
# Where,
#	R ... estimated rate of star creation in our galaxy
#	p ... estimated percent of stars that have planets
#	n ... estimated average numer of planets that can potentially
#		  support life for each star with planets
#	f ... estimated percent of those planets that actually go on to 
#		  develop life
#	i ... estimated percent of those planets that go on to develop 
#		  intelligent life
#	c ... estimated percent of those that are willing and able to 
#		  communicate
#	L ... estimated expected lifetime of such civilizations

# display program welcome
print('Welcome to the SETI program')
print('This program will allow you to enter specific values related to')
print('the likelyhood of finding intelligent life in our galaxy. All')
print('percentages should be entered as integer values, e.g., 40 not .40')
print()

# get user input
p = 1
n = int(input('How many planets per star do you think can support life?: '))
f = 1
i = 1
c = 1
L = int(input('Number of years you think civilizations last?: '))

# calculate result
num_detectable_civilizations = 7 * p * n * f * i * c * L

# display result
print()
print('Based on the values entered ...')
print('there are an estimated', round(num_detectable_civilizations), 
	'potentially detectable civilizations in our galaxy')
