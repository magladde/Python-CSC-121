# Largest number program

# program introduction
print('This program takes user input for three numbers and selects the')
print('largest one.')

# get user input
num_one = float(input('Enter first number: '))
num_two = float(input('Enter second number: '))
num_three = float(input('Enter thrid number: '))

# compare to min
if num_one >= num_two and num_one >= num_three:
	largest_number = num_one
	
elif num_two >= num_one and num_two >= num_three:
	largest_number = num_two
	
else:
	largest_number = num_three
	
# print output
print('The largest number is: ', largest_number)
