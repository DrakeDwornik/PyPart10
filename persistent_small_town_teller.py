import random
class Person():
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Account():
    def __init__(self, acct_number, type, owner):
        self.number = acct_number
        self.type = type
        self.owner = owner
        self.balance = 0.0


class Bank():
    def __init__(self):
        self.customers_list = {}
        self.accounts_list = {}

    def add_customer(self, first_name, last_name):
        id = random.randrange(10000)
        while id in self.customers_list:
            id = random.randrange(10000)
        self.customers_list[id] = Person(id, first_name, last_name)



    def add_account(self, type, owner_id):
        acct_number = random.randrange(10000)
        if owner_id not in self.customers_list:
            print("invalid customer id, try again")
        while acct_number in self.accounts_list:
            id = random.randrange(10000)
        self.accounts_list[acct_number] = Account(acct_number, type, owner_id)

    def remove_account(self, number):
        del self.accounts_list[number]

    def deposit(self, acct_number, amount):
        self.accounts_list[acct_number].balance += amount

    def withdraw(self, acct_number, amount):
        self.accounts_list[acct_number].balance -= amount

    def balance(self, acct_number):
        print(self.accounts_list[acct_number].balance)
