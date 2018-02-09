# display 1 - 100

# program introduction
print('This program prints the numbers 1 - 100 in a grid pattern.')
print('This is accomplished via a pair of nested while loops.')
print()

# print 1 - 100 in a grid pattern

row = 0
number = 1
column = 0
while row < 10:
	while column < 10:
		if number < 10:
			print(format(' ', '3'), number, end = " ")
			number = number + 1
			column = column + 1
		else:
			print(format(' ', '2'), number, end = " ")
			number = number + 1
			column = column + 1
	print()
	column = 0
	row = row + 1
