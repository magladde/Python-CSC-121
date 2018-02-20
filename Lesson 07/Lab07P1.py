# Wake Tech. CSC 121 Lesson 7 Problem 1

# main function, get number of kWh used, pass kWh used to 
# bill_calculator function.
def main():
	kilowatts_used = int(input('Enter kilowatt hours used: '))
	bill_calculator(kilowatts_used)

# bill_calculator function, rate is $0.12 per kWh for the first 500 kWh,
#$0.15 per kWh after 500 kWh
def bill_calculator(x):
	if x > 500:
		bill = (500 * .12) + ((x - 500) * .15)
	else:
		bill = x * .12
	print('Please pay this amount:', bill)

# call main function
main()
