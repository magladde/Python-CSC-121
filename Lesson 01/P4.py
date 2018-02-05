# This program takes a user entered binary number that is four-digits
# long and converts it into its base 10 eqivalent.

first_digit = int(input('Enter left most digit: '))
second_digit = int(input('Enter the next digit: '))
third_digit = int(input('Enter the next digit: '))
fourth_digit = int(input('Enter the next digit: '))

base_10_equivalent = (first_digit * 8) + (second_digit * 4) + (third_digit * 2) + (fourth_digit * 1)

print('The value is', base_10_equivalent)
