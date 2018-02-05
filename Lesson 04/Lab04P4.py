# Salary calculator program

# program introduction
print('Instructors at a community college are paid on a schedule that')
print('provides a salary based on their number of years of teaching ')
print('experience. For each year experience after the first year, up')
print('to 10 years, the instructor receives 2% increase over the ')
print('preceding value. Instructors are also required to deposit ')
print('5% of the salary each year into a retirement fund account.')
print()
print('This program takes user input of starting salary and calculates')
print('the rise in salary, and retirement fund total over 10 years.')
print()

# get user input for starting salary
starting_salary = float(input('Enter starting salary: '))
first_year_retirement = starting_salary * .05

# enter first year values
print('Year: 1 Salary: ' + str(starting_salary))
print('Retirement Fund Total So Far: ' + str(first_year_retirement))
print()

# enter loop calculating salary and retirement fund total
counter = 1
yearly_salary = starting_salary
retirement_total = first_year_retirement
while counter < 10:
	yearly_salary = yearly_salary + (yearly_salary * .02)
	retirement_payment = yearly_salary * .05
	retirement_total = retirement_total + retirement_payment
	
	print('Year: ' + str((counter + 1)) + ' Salary: ' + \
		str(yearly_salary))
	print('Retirement Fund Running Total: ' + \
		str(retirement_total))
	print()
	counter = counter + 1
