# lab 5 problem 2

# program introduction
print('This program simulates course registration. Users can add and ')
print('drop courses. The program will display error messages and the')
print('courses choosen by the user.')
print()

# get user input for the courses
course_catalog = []
user_input = 'A'
while user_input != 'E':
	user_input = input('Enter A to add course, D to drop course, and E to exit: ')
	if user_input == 'A':
		course = input('Enter course to add: ')
		if course in course_catalog:
			print('You are already registered in that course.')
			print()
		else:
			course_catalog.append(course)
			course_catalog.sort()
			print('Course added')
			print('Courses registered: ', course_catalog)
			print()
	elif user_input == 'D':
		drop_course = input('Enter course to drop: ')
		if drop_course in course_catalog:
			course_catalog.remove(drop_course)
			course_catalog.sort()
			print('Course dropped')
			print('Courses registered: ', course_catalog)
			print()
