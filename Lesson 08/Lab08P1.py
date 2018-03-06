# Lesson 08 lab problem 1
def main():
    kWh = get_kWh_used()
    bill = bill_calculator(kWh)
    print('Please pay this amount:', bill)

def get_kWh_used():
    kWh = int(input('Enter kilowatt hours used: '))
    while kWh < 0:
        print('kWh cannot be negative.')
        kWh = int(input('Enter kilowatt hours used: '))
    return(kWh)

def bill_calculator(x):
    if x < 500:
        bill = x * .12
    else:
        bill = (500 * .12) + (x - 500) * .15
    return bill

main()