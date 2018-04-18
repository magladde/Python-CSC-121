class Account:

    def __init__(self, name, acct_num):

        """ constructor """

        self.name = name
        self.acct_num = acct_num
        self.balance = 0

    def deposit(self, amt):

        """ deposit money in the account """

        self.balance = self.balance + amt

    def withdraw(self, amt):

        """ withdraw money from the account """

        if amt > self.balance:
            print("Withdrawal denied due to insufficient fund.")
        else:
            self.balance = self.balance - amt
