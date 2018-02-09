# lab 5 program 4

# program introduction
print('This program generates two lists of randomly generated numbers')
print('and then compares the lists to see which number was higher at ')
print('each position in the list.')
print()

# generate first list of randomly generated numbers and display list
import random

list_one = []
for i in range(5):
	num = random.randint(1, 9)
	list_one.append(num)
print('First list: ', list_one)

# generate second list of randomly generated numbers and display list
list_two = []
for i in range(5):
	num = random.randint(2, 8)
	list_two.append(num)
print('Second list: ', list_two)

# compare each position in list_one and list_two and display the
# larger value sequentially
print('Larger number in each comparison: ')
i = 0
length = len(list_one)
for value in list_one:
	if value > list_two[i]:
		print(value)
	else:
		print(list_two[i])
	i = i + 1
	
