# Bounciness index program

# program introduction
print('This program takes user input in the form of the initial ')
print('height of a ball dropped. The bounciness index, and the number')
print('of times the ball is allowed to bounce. The program then ')
print('calculates the height of each subsequent bounce.')

# get userinput
initial_height = int(input('Enter initial height: '))
bounciness_index = float(input('Enter bounciness index: '))
num_bounces = int(input('Enter number of times the ball is allowed ' +\
	'to bounce: '))
	
# calculate height bounced
counter = 0
height = initial_height
while counter < num_bounces:
	counter = counter + 1
	height = height * bounciness_index
	print('Number of bounces: ' + str(counter) + ' Height: ' + str(height))
