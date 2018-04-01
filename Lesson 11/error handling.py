# problem 1
try:
    salary = float(input('Enter annual salary: '))
    salary = salary + salary * .05
    print('New salary: ', salary)
except ValueError:
    print('Salary must be a numerical value with no commas.')