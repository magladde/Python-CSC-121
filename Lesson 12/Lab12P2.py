# Lab 12 problem 2
import currency

def main():
    """ This program converts USD to one of three foreign currencies """


    print('Converting US Dollar to a foreign currency.')

    currency_to_convert = int(input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: '))
    while currency_to_convert not in [1, 2, 3]:
        print('Error: Invalid choice')
        currency_to_convert = int(input('Enter 1 for Euro, 2 for Japanese Yen, 3 for Mexican Peso: '))

    us_dollar_amount = int(input('Enter US Dollar: '))
    while us_dollar_amount < 0:
        print('Error: US Dollar cannot be negative.')
        us_dollar_amount = int(input('Enter US Dollar: '))

    if currency_to_convert == 1:
        converted_amount = currency.to_euro(us_dollar_amount)
        print('It is converted to', converted_amount, 'Euro')
    elif currency_to_convert == 2:
        converted_amount = currency.to_yen(us_dollar_amount)
        print('It is converted to', converted_amount, 'Yen')
    else:
        converted_amount = currency.to_peso(us_dollar_amount)
        print('It is converted to', converted_amount, 'Peso')

main()