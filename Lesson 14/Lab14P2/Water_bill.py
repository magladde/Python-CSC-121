from Utility_bill import Utility_bill


class Water_bill(Utility_bill):

    def __init__(self, name, address):
        base = super()
        base.__init__(name, address)
        self._num_gal = 0

    def calculate_charge(self):
        self._num_gal = int(input('How many gallons of water were used? '))
        print()
        if self._num_gal <= 6000:
            self._total = .005 * self._num_gal
        elif self._num_gal > 6000:
            self._total = (.005 * 6000) + (self._num_gal - 6000) * .007

    def display_bill(self):
        print('Water Bill')
        print('Name:', self._name)
        print('Address:', self._address)
        print('Gallons used:', self._num_gal)
        print('Please pay this amount:', self._total)
