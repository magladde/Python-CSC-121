# Lesson 6 Lab problem 2

# program introduction
print('This program will generate 10 random integers between numbers 1')
print('and 15. These integers will be stored in a tuple, which will be')
print('displayed. The program will create a new tuple and store the ')
print('first three elements from the first tuple into the new tuple.')
print('The program will then create a third tuple and store the last')
print('three elements from the first tuple into this third tuple.')
print('Next the program will concatenate the second and third tuple,')
print('display the concatenated tuple, sort the concatenated tuple,')
print('and finnally display the sorted tuple.\n')

# generate tuple_one and display tuple_one
import random

list_one = []
for i in range(10):
	num = random.randint(1, 15)
	list_one.append(num)
tuple_one = tuple(list_one)
print('Tuple of 10 random numbers:', tuple_one)

# store the first three elements of tuple_one in new tuple, tuple_two
list_two = []
for i in range(3):
	list_two.append(tuple_one[i])
tuple_two = tuple(list_two)
print('Tuple of first 3 numbers:', tuple_two)

# store the last three elements of tuple_one in a new tuple, tuple_three
list_three = []
for i in range(3):
	list_three.append(tuple_one[7 + i])
tuple_three = tuple(list_three)
print('Tuple of last 3 numbers:', tuple_three)

# concatenate tuple_2 and tuple_3, display, sort, and redisplay
# concatenated tuple
concat_tuple = tuple_two + tuple_three
print('Two tuples concatenated:', concat_tuple)
concat_list = list(concat_tuple)
concat_list.sort()
concat_tuple = tuple(concat_list)
print('Two tuples concatenated and sorted:', concat_tuple)
	
