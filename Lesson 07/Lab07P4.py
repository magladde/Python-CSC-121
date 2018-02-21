# Wake Tech. CSC 121 Lesson 7 Problem 4
# This program calculates a course grade using two functions

# define main function, prompt user for how many labs there are. Use a loop
# to enter lab scores and store in a list, display lab scores. Perform
# the same for tests. Get the weights for labs and tests (default weights
# are 50 percent and 50 percent). Call grade_calculator function
def main():
	lab_scores = []
	test_scores = []
	num_labs = int(input('How many labs? '))
	for i in range(num_labs):
		lab_score = int(input('Enter a lab score: '))
		lab_scores.append(lab_score)
	print('Lab scores:', lab_scores)
	
	num_tests = int(input('How many tests? '))
	for i in range(num_tests):
		test_score = int(input('Enter a test score: '))
		test_scores.append(test_score)
	print('Test scores:', test_scores)
	print()
	
	print('The default weights for course grade are 50% labs and 50% tests.')
	weight = input('Enter C to change the weights or D to use default weights: ')
	if weight == 'C':
		lab_weight = int(input('Enter lab percentage (without the % sign): '))
		test_weight = int(input('Enter test percentage (without the % sign): '))
		grade_calculator(lab_scores, test_scores, lab_weight, test_weight)
	elif weight == 'D':
		grade_calculator(lab_scores, test_scores)
	
# define grade_calculator function
def grade_calculator(lab_scores, test_scores, lab_percent = .5, test_percent = .5):
	# calculate lab average
	total = 0
	for score in lab_scores:
		total = total + score
	lab_average = total / len(lab_scores)
	print('Lab average:', lab_average)
	
	# calculate test average
	total = 0
	for score in test_scores:
		total = total + score
	test_average = total / len(test_scores)
	print('Test average:', test_average)
	
	# calculate course grade
	lab_portion = lab_average * lab_percent / 100
	test_portion = test_average * test_percent / 100
	course_grade = lab_portion + test_portion
	print('Course grade:', course_grade)

# call main function		
main()
