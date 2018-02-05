# Water rate calculator

# program introduction
print('This program calculates what the water bill would be given')
print('user input. User should choose whether they are a residential')
print('or a buisness customer. Then the user should input their usage')
print('in gallons.')

# get user input
customer_type = input('\nEnter R for residential customer or B for'
	+ 'business customer: ')
customer_type = customer_type.lower()

gallons_used = int(input('How many gallons of water were used? '))

# calculate water bill
residential_rate_one = .005
residential_rate_two = .007
business_rate_one = .006
business_rate_two = .008

if customer_type == 'r':
	if gallons_used < 6000:
		water_bill = gallons_used * residential_rate_one
	else:
		water_bill = ((gallons_used - 6000) * residential_rate_two) \
			+ (6000 * residential_rate_one)
else:
	if gallons_used < 8000:
		water_bill = gallons_used * business_rate_one
	else:
		water_bill = ((gallons_used - 8000) * business_rate_two) \
			+ (8000 * business_rate_one)
			
# display output
print('Please pay this amount: $' + str(water_bill))
