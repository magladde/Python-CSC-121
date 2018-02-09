# Lab 5 program 3

# program introduction
print('This program uses the range function to generate a sequence of')
print('integers: 5, 9, 13, 17, and 21. Then we will store this')
print('sequence in a list, display the list, use a for loop to display')
print('each element in a separate line. We will then use the range')
print('function to generate a new sequence of integers: 26, 19, 12,')
print('and 5. Then we will store this sequence in a list, display the')
print('list, use a for loop to calculate the total of the elements and')
print('display the total.')
print()

# use range to generate first sequence of integers, use list to move
# integers into a list, print list and each element on a single line
sequence_one = range(5, 22, 4)
sequence_one_list = list(sequence_one)
print('First list: ', sequence_one_list)
print('Elements in the first list: ')
for element in sequence_one_list:
	print(element)

# use range to generate second sequence of integers, use list to move
# integers into a list, print list and calculate total of those
# element
sequence_two = range(26, 4, -7)
sequence_two_list = list(sequence_two)
print('Second list: ', sequence_two_list)
total = 0
for element in sequence_two_list:
	total = total + element
print('Total of the elements in the second list: ', total)
