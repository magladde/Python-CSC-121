class Account:

    def __init__(self, name, acct_num):

        """ constructor """

        self.__name = name
        self.__acct_num = acct_num
        self.__balance = 0


    def deposit(self, amt):

        """ deposit money into the account """

        self.__balance = self.__balance + amt

    def withdraw(self, amt):

        """ withdraw money from the account """

        if amt > self.__balance:
            print('Withdrawal denied to insufficient fund.')
        else:
            self.__balance = self.__balance - amt

    def getBalance(self):
        return self.__balance