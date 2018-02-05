# This program takes user input for a base and an exponent. The program
# then calculates the user base raised to the user exponent.

user_base = int(input('What base? '))
user_exponent = int(input('What power of 10? '))
calculated_value = user_base ** user_exponent
print(user_base, 'to the power of', user_exponent, 'is', calculated_value)
