# example 1
book = 'Introduction to Computer Science using Python'
num_spaces = 0
for chr in book:
    if chr == ' ':
        num_spaces = num_spaces + 1
print('Number of spaces:', num_spaces)
print('\n')

# example 2
college = "Wake Tech"
length = len(college)
print("Length of string:", length)
print('\n')

# example 3
college = "Wake Tech"
third_char = college[2]
print('The third character in the string is:', third_char)
print('\n')

# example 4
college = "Wake Tech"
first_word = college[0:4]
second_word = college[5:9]
print('First word in the string:', first_word)
print('Second word in the string:', second_word)
print('\n')

# example 5
college = "Wake Tech"
num_e = college.count("e")
print("The number of e's in 'Wake Tech':", num_e)
print('\n')

# example 6
college = "Wake Tech"
first_e = college.index('e')
print("Index number of first e in 'Wake Tech':", first_e)
print('\n')

# example 7
college = "Wake Tech"
if 'e' in college:
    print('The letter e is found in Wake Tech')
else:
    print('The letter e is not found in Wake Tech')
print('\n')

# example 8
card_num = input('Please enter your 16-digit card number: ')
while not card_num.isdigit():
    print('Invalid card number.')
    card_num = input('Please enter your 16-digit card number: ')
print('Card number entered:', card_num)