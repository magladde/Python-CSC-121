from Utility_bill import Utility_bill


class Electricity_bill(Utility_bill):

    def __init__(self, name, address):
        base = super()
        base.__init__(name, address)
        self._num_kWh = 0

    def calculate_charge(self):
        self._num_kWh = int(input('Enter kilowatt hours used: '))
        print()
        if self._num_kWh <= 500:
            self._total = self._num_kWh * .12
        elif self._num_kWh > 500:
            self._total = (500 * .12) + (self._num_kWh - 500) * .15

    def display_bill(self):
        print('Electricity Bill')
        print('Name:', self._name)
        print('Address:', self._address)
        print('Kilowatt Hours used:', self._num_kWh)
        print('Please pay this amount:', self._total)
