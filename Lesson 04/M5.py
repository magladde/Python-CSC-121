# Oil Change Notification Program

# display program welcome
print('This program will determine if your car is in need of an oil change')

# init
miles_between_oil_change = 7500 # num miles between oil changes
miles_warning = 500				# how soon to warn of needed oil change
valid_entries = False

# get mileage of last oil change and current mileage and display
while not valid_entries:
	mileage_last_oilchange = int(input('Enter mileage of last oil change: '))
	current_mileage = int(input('Ener current mileage: '))
	
	if current_mileage < mileage_last_oilchange:
		print('Invalid entry - current mileage entered is less than')
		print('mileage entered of last oil change')
	else:
		miles_traveled = current_mileage - mileage_last_oilchange
		valid_entries = True
		
if miles_traveled >= miles_oil_change:
	print('You are due for an oil change')
elif miles_traveled >= miles_oil_change - miles_warning:
	print('You will soon be due for an oil change')
else:
	print('You are not in immediate need of an oil change')
