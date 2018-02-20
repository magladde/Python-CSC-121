# Wake Tech. CSC 121 Lesson 7 Problem 2

# define main function, get number of kWh used, customer type (buisiness 
# or residential) pass kWh used and customer type to bill_calculator 
# function.
def main():
	kilowatt_used = int(input('Enter kilowatt hours used: '))
	customer_type = input('Enter R for residential customer, B for '  
		'business customer: ')
	bill_calculator(kilowatt_used, customer_type)

# define bill_calculator function, rate is $0.12 per kWh for the first 
# 500 kWh, $0.15 per kWh after 500 kWh
def bill_calculator(kilowatt, cust_type):
	if cust_type == 'R':
		if kilowatt < 500:
			bill = kilowatt * .12
		else:
			kilowatt = kilowatt - 500
			bill = (500 * .12) + (kilowatt * .15)
		print('Please pay this amount: ' + str(bill))
	elif cust_type == 'B':
		if kilowatt < 800:
			bill = kilowatt * .16
		else:
			kilowatt = kilowatt - 800
			bill = (800 * .16) + (kilowatt * .2)
		print('Please pay this amount: ' + str(bill))

# call main function
main()
