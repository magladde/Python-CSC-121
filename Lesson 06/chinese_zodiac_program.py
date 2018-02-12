# Chinese Zodiac Program

import datetime

# init
zodiac_animals = ('Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake',
				  'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig')

rat = 'Forthright, industrious, sensitive, intellectual, sociable'
ox = 'Dependable, methodical, modest, born leader, patient'
tiger = 'Unpredictable, rebellious, passionate, daring, impulsive'
rabbit = 'Good friend, kind, soft-spoken, cautious, artistic'
dragon = 'Strong, self-assured, proud, decisive, loyal'
snake = 'Deep thinker, creative, responsible, calm, purposeful'
horse = 'Cheerful, quick-witted, perceptive, talkative, open-minded'
goat = 'Sincere, sympathetic, shy, generous, mothering'
monkey = 'Motivator, inquisitive, flexible, innovative, problem solver'
rooster = 'Organized, self-assured, decisive, perfectionist, zealous'
dog = 'Honest, unpretentious, idealistic, moralistic, easy going'
pig = 'Peace-loving, hard-working, trusting, understanding,thoughtful'

characteristics = (rat, ox, tiger, rabbit, dragon, snake, horse, goat,
				   monkey, rooster, dog, pig)
terminate = False

# program greeting
print('This program will display your Chinese zodiac sign and associated')
print('personal characteristics. \n')

# get current year from module datetime
current_yr = datetime.date.today().year

while not terminate:
	
	# get year birth
	birth_year = int(input('Enter your year of birth (yyyy): '))
	
	while birth_year < 1900 or birth_year > current_yr:
		print('Invalid year. Please re-enter\n')
		birth_year = int(input('Enter your year of birth (yyyy): '))
		
	# output results
	cycle_num = (birth_year - 1900) % 12
	
	print('Your Chinese zodiac sign is the', zodiac_animals[cycle_num],'\n')
	print('Your personal characteristics ...')
	print(characteristics[cycle_num])
	
	# continue?
	user_response = input('\nWould you like to enter another year? (y/n): ')
	
	while user_response != 'y' and user_response != 'n':
		user_response = input("Please enter 'y' or 'n': ")
	
	if user_reponse == 'n':
		terminate = True
