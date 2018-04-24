class Account:

    def __init__(self, name, acct_num):
        self.__name = name
        self.__acct_num = acct_num
        self.__balance = 0

    def deposit(self, amt):
        self.__balance = self.__balance + amt

    def withdraw(self, amt):
        if amt > self.__balance:
            print('Withdrawal denied due to insufficient fund.')
        else:
            self.__balance = self.__balance - amt

    def getBalance(self):
        return self.__balance

    def __str__(self):
        return 'Account name: ' + self.__name + '\nAccount number: ' + \
               self.__acct_num + '\nBalance: ' + str(self.__balance)