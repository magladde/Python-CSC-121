# Lesson 6 Lab Problem 1

# program introduction
print('This program takes user input in the form of test scores. The')
print('program stores these scores in a list and displays the list.')
print('The program then copies the scores to a new list. Once in the')
print('new list each score is examined and if below 60, 10 points are')
print('added. The new list is then displayed. Finnally the program ')
print('compares the original score to the new score and displays the ')
print('two scores if they are different.\n')

# get user input for test scores and put into first_list
first_list = []
for k in range(5):
	test_score = int(input('Enter a test score: '))
	first_list.append(test_score)
print('All scores: ', first_list)

# generate second list, and add 10 points if the value is below 60
print('Students who scored below 60 get 10 extra points.')
second_list = first_list[:]
for k in range(len(first_list)):
	if second_list[k] < 60:
		second_list[k] = second_list[k] + 10
print('All scores: ', second_list)

# compare first_list to second_list and display if values are different
print('Students whose scores have changed: ')
for k in range(len(first_list)):
	if first_list[k] != second_list[k]:
		print('Old score:', first_list[k], 'New score:', second_list[k])
