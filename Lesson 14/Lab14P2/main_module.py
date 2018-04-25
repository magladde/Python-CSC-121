from Water_bill import Water_bill
from Electricity_bill import Electricity_bill


def main():
    name = input('Enter name: ')
    address = input('Enter address: ')
    bill_type = int(input('Enter 1 for water bill, 2 for electricity bill: '))

    if bill_type == 1:
        water_bill = Water_bill(name, address)
        water_bill.calculate_charge()
        water_bill.display_bill()
    elif bill_type == 2:
        electricity_bill = Electricity_bill(name, address)
        electricity_bill.calculate_charge()
        electricity_bill.display_bill()


main()
