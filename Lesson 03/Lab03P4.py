# Shipping program

# shipping rates
standard_rate_one = 1.05
standard_rate_two = .95
standard_rate_three = .85
standard_rate_four = .80

express_rate_one = 3.25
express_rate_two = 2.95
express_rate_three = 2.75
express_rate_four = 2.55

# program introduction rates
print('A shipping company allows customers to choose between standard')
print('or express delivery. Standard deliveries are charged at the ')
print('following rates:')
print('\n4 pounds or less: 				$' + str(standard_rate_one))
print('Over 4 pounds but no more than 8 pounds: 	$' + \
	str(standard_rate_two))
print('Over 8 pounds but no more than 15 pounds: 	$' + \
	str(standard_rate_three))
print('Over 15 pounds: 				$' + format(standard_rate_four, '.2f'))
print('\nExpress deliveries are charged the following rates:')
print('\n2 pounds or less: 				$' + str(express_rate_one))
print('Over 2 pounds but no more than 5 pounds: 	$' + \
	str(express_rate_two))
print('Over 5 pounds but no more than 10 pounds: 	$' + \
	str(express_rate_three))
print('Over 10 pounds:					$' + str(express_rate_four))

# get user input for shipping type and weight
print('\nPlease pick either Standard or Express shipping and input')
print('weight in pounds.')

shipping_type = input('Enter S for standard shipping, E for express: ')
shipping_type = shipping_type.lower()

shipping_weight = float(input('Enter weight(lbs): '))

# calculate shipping cost
if shipping_type == 's':
	if shipping_weight <= 4:
		shipping_rate = standard_rate_one
	elif 4 < shipping_weight <= 8:
		shipping_rate = standard_rate_two
	elif 8 < shipping_weight <= 15:
		shipping_rate = standard_rate_three
	else:
		shipping_rate = standard_rate_four
else:
	if shipping_weight <= 2:
		shipping_rate = express_rate_one
	elif 2 < shipping_weight <= 5:
		shipping_rate = express_rate_two
	elif 5 < shipping_weight <= 10:
		shipping_rate = express_rate_three
	else:
		shipping_rate = express_rate_four

shipping_charge = shipping_weight * shipping_rate

# display output
print('Shipping charge: $' + str(shipping_charge))

