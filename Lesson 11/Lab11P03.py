# Lab 11 problem 3

def main():
    # variable for item cost
    hotdog_price = 2.5
    chip_price = 1.5
    soda_price = 1.25

    # get number of hotdogs, chips, and sodas ordered
    try:
        num_dog = int(input('How many hotdogs? '))
    except ValueError:
        print('Invalid input. Number of hotdogs set to 0.')
        num_dog = 0
    try:
        num_chip = int(input('How many bags of chips? '))
    except ValueError:
        print('Invalid input. Number of chips set to 0.')
        num_chip = 0
    try:
        num_soda = int(input('How many cans of soda? '))
    except ValueError:
        print('Invalid input. Number of sodas set to 0.')
        num_soda = 0

    # calculate total cost
    total_cost = (hotdog_price * num_dog) + (chip_price * num_chip) + (soda_price * num_soda)

    # display total cost
    print('Please pay this amount:', total_cost)

main()