# Wake Tech. CSC 121 Lesson 7 Problem 3

# define main function, get number of kWh used, customer type (buisiness 
# or residential) pass kWh used and customer type to bill_calculator 
# function.
def main():
	kilowatt_used = int(input('Enter kilowatt hours used: '))
	customer_type = input('Enter R for residential customer, B for '  
		'business customer: ')
	bill_calculator(x1 = kilowatt_used, x2 = customer_type)

# define bill_calculator function, rate is $0.12 per kWh for the first 
# 500 kWh, $0.15 per kWh after 500 kWh
def bill_calculator(x1, x2):
	if x2 == 'R':
		if x1 < 500:
			bill = x1 * .12
		else:
			x1 = x1 - 500
			bill = (500 * .12) + (x1 * .15)
		print('Please pay this amount: ' + str(bill))
	elif x2 == 'B':
		if x1 < 800:
			bill = x1 * .16
		else:
			x1 = x1 - 800
			bill = (800 * .16) + (x1 * .2)
		print('Please pay this amount: ' + str(bill))

# call main function
main()
