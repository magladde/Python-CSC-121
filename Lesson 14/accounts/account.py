class Account:

    def __init__(self, name, acct_num):
        self.name = name
        self.acct_num = acct_num
        self.balance = 0

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        if amt > self.balance:
            print('Withdrawal denied due to insufficient fund.')
        else:
            self.balance = self.balance - amt

    def __str__(self):
        return 'Account name: ' + self.name + '\nAccount number: ' + \
               self.acct_num + '\nBalance: ' + str(self.balance)