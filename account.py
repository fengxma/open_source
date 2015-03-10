class Account(object):
    # num_accounts is a class variable that's shared among all the instances
    #  but not assigned to each instance
    num_accounts = 0
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_accounts += 1
    def __del__(self):
        Account.num_accounts -= 1
    def deposit(self, amt):
        self.balance = self.balance + amt
    def withdraw(self, amt):
        self.balance = self.balance - amt
    def inquiry(self):
        return self.balance