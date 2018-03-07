# Lesson 08 lab problem 3
print('This program creates a list of odd numbers in the range of your choice.')
start_num = int(input('Enter a starting number: '))
end_num = int(input('Enter ending number: '))
my_list = list(num for num in range(start_num, end_num + 1) if num % 2 == 1)
print('odd numbers in the range:', my_list)