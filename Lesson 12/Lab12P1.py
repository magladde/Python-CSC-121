# Lab 12 problem 1

def main():
    """ This program simulates a self-checkout system """

    print('Welcome to the self-checkout system of Wake-mart.')

    num_items, total_cost = scanPrices()

    total_cost = discount(num_items, total_cost)

    num_items, total_cost = promotion(num_items, total_cost)

    makePayment(total_cost)


def scanPrices():
    """ This function takes user input for the prices of items to be purchased """

    total = 0
    loop_counter = 0
    user_input = float(input('Enter price of first item [or 0 to stop]: '))
    while user_input != 0:
        if user_input > 0:
            loop_counter = loop_counter + 1
            total = total + user_input
            print('Number of items:', loop_counter, 'Total:', total)
            user_input = float(input('Enter price of next item [or 0 to stop]: '))
        else:
            print('Price cannot be negative')
            user_input = float(input('Enter price of next item [or 0 to stop]: '))

    return (loop_counter, total)


def discount(count, total):
    """ This function gives a 10% discount if 10 or more items are purchased """

    if count > 9:
        print()
        total = total * .9
        print("You've got 10% discount for buying 10 items or more.")
        print('Number of items:', count, 'Total:', total)

    return total


def promotion(count, total):
    """ This function allows the user to purchase a 50 dollar gift card. If the total is higher than
        50 dollars the gift card is discounted to 40 dollars"""

    print()
    if total >= 50:
        gift_card = input('Do you want to buy a $50 gift card for $40? [y/n] ')
        if gift_card == 'y':
            total = total + 40
            count = count + 1
            print('Thank you for buying a gift card.')
            print('Number of items:', count, 'Total:', total)
    else:
        gift_card = input('Do you want to buy a $50 gift card [y/n] ')
        if gift_card == 'y':
            total = total + 50
            count = count + 1
            print('Thank you for buying a gift card.')
            print('Number of items:', count, 'Total:', total)

    return (count, total)


def makePayment(balance):
    """ This function takes previously calculated total (balance) and then takes user input
        to determine if user is pyaing with cash or debit. This function then takes balance
        and sends it to the appropriate payment function. """

    print()
    print('Payment options:')
    payment_type = int(input('Enter 1 for cash, 2 for debit: '))
    if payment_type == 1:
        payCash(balance)
    else:
        payDebit(balance)


def payCash(balance):
    """ This function takes the balance and walks the user how to pay by cash.
        The self-checkout machine only accepts 10, 5, and 1 dollar bills.

        If customer pays more than the balance calculate and display change """

    print('This machine only accepts $10, $5, and $1 dollar bills.')
    num_tens = int(input('How many $10 bills are you going to use? '))
    num_fives = int(input('How many $5 bills are you going to use? '))
    num_ones = int(input('How many $1 bills are you going to use? '))

    total_payment = (num_tens * 10) + (num_fives * 5) + (num_ones * 1)

    while total_payment < balance:
        print()
        print('Error: Total cash payment less than balance. Please reenter.')
        num_tens = int(input('How many $10 bills are you going to use? '))
        num_fives = int(input('How many $5 bills are you going to use? '))
        num_ones = int(input('How many $1 bills are you going to use? '))

        total_payment = (num_tens * 10) + (num_fives * 5) + (num_ones * 1)

    if total_payment > balance:
        print('Thank you for your payment.')
        print('Change:', total_payment - balance)
    else:
        print('Thank you for your payment.')


def payDebit(balance):
    """ This function allows user to pay with a credit card. Function takes user input for card number, card pin, and
        payment amount. Validation loop confirms that payment amount and balance are the same"""

    card_num = int(input('Please enter a 16-digit card number: '))
    card_pin = int(input('Please enter 4-digit pin: '))
    payment_amount = float(input('Please enter payment amount: '))
    if payment_amount != balance:
        print('ERROR: Payment amount cannot be smaller than balance')
        payment_amount = float(input('Please enter payment amount:'))
    print('Thank you for your payment.')


main()
