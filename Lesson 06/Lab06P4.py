# Lesson 6 Lab 4

# This program will generate a list of powers using list comprehension
# This program will generate the fist, second, third and fourth powers
# of 2, store the results in a list, and display the list. This program
# will also do the same for the first four powers of 3. Lastly this
# program will generate a matrix of the first four powers for 2, 3, 4, 
# 5, and 6 using nested list comprehension

# generate power of 2 list using list comprehension
powers_two = [2 ** i for i in range(1,5)]
print('Powers of 2:', powers_two)

# generate power of 3 list using list comprehension
powers_three = [3 ** i for i in range(1,5)]
print('Powers of 3:', powers_three)

# generate matrix
matrix = [[x ** y for y in range(1,5)] for x in range(2,7)]
print(matrix)
