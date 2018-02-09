# coin change exercise program

import random

# program greeting
print('The purpose of this exercise is to enter a number of coin values')
print('that add up to a displayed target value. \n')
print('Enter coin values as 1-penny, 5-nickle, 10-dime, 25-quarter, and 50-half dollar')
print('Hit return after the last entered coin value.')
print('----------------')

# init
terminate = False
empty_str = ''

# start game
while not terminate:
	amount = random.randint(1,99)
	print('Enter coins that add up to', amount, 'cents, one per line.\n')
	game_over = False
	total = 0
	
	while not game_over:
		valid_entry = False
		
		while not valid_entry:
			if total == 0:
				entry = input('Enter first coin: ')
			else:
				entry = input('Enter next coin: ')
			
			if entry in (empty_str, '1', '5', '10', '25', '50'):
				valid_entry = True
			else:
				print('Invalid entry')
				
		if entry == empty_str:
			if total == amount:
				print('Correct!')
			else: 
				print('Sorry - you only entered', total, 'cents.')
			
			game_over = True
		else:
			total = total + int(entry)
			if total > amount:
				print('Sorry - total amount exceeds', amount, 'cents.')
				game_over = True
				
		if game_over:
			entry = input('\nTry again (y/n)?: ')
			
			if entry == 'n':
				terminate = True
				
print('Thanks for playing ... goodbye')
