# Lab 5 problem 1 

# program introduction
print('This program takes user input in the form of as many integers')
print('that the user wants, from 1-10. These integers will be stored in')
print('a list. The list will be displayed, along with the average and ')
print('if the average is higher than 7 we will subtract 1 from every ')
print('number in the list then display the modified list.')
print()

# get user input
again = 'y'
num_list = []
while again == 'y':
	user_input = int(input('Enter an integer from 1 to 10: '))
	num_list.append(user_input)
	again = input('Enter another integer? [y/n] ')
	
# display the list generated by the user
print('Number list: ' + str(num_list))

# calculate average of the user generated list
length = len(num_list)
total = 0
for integer in num_list:
	total = total + integer
average = total / length

# display average
print('Average: ', average)

# modify list if average is greater than 7
if average > 7:
	i = 0
	while i < length:
		num_list[i] = num_list[i] - 1
		i = i + 1

# print modified list
print(num_list)
