# Lesson 08 lab problem 2
def main():
    kWh, cust_type = get_user_input()
    bill = bill_calculator(kWh, cust_type)
    print('Please pay this amount:', bill)

def get_user_input():
    kWh = int(input('Enter kilowatt hours used: '))
    while kWh < 0:
        print('kWh cannot be negative.')
        kWh = int(input('Enter kilowatt hours used: '))

    cust_type = input('Enter R for residential customer, B for business customer: ')
    cust_type = cust_type.upper()
    while cust_type != 'R' and cust_type != 'B':
        print('Invalid customer type.')
        cust_type = input('Enter R for residential customer, B for business customer: ')
        cust_type = cust_type.upper()
    return kWh, cust_type

def bill_calculator(kWh, cust_type):
    if cust_type == 'R':
        if kWh < 500:
            bill = kWh * .12
        else:
            bill = (500 * .12) + (kWh - 500) * .15
    else:
        if kWh < 800:
            bill = kWh * .16
        else:
            bill = (800 * .16) + (kWh - 800) * .2
    return bill
main()