# Lab 11 problem 4
def main():
    # variable for item cost
    hotdog_price = 2.5
    chip_price = 1.5
    soda_price = 1.25

    num_dog = get_dogs()
    num_chip = get_chips()
    num_soda = get_sodas()

    total = (hotdog_price * num_dog) + (chip_price * num_chip) + (soda_price * num_soda)

    print('Please pay this amount:', total)

def get_dogs():
    is_error = False
    while not is_error:
        try:
            num_dog = int(input('How many hotdogs? '))
            is_error = True
        except ValueError:
            print('Invalid input.')
    return num_dog

def get_chips():
    is_error = False
    while not is_error:
        try:
            num_chip = int(input('How many chips? '))
            is_error = True
        except ValueError:
            print('Invalid input.')
    return num_chip

def get_sodas():
    is_error = False
    while not is_error:
        try:
            num_soda = int(input('How many sodas? '))
            is_error = True
        except ValueError:
            print('Invalid input.')
    return num_soda


main()