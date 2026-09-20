class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")


account1 = BankAccount(5000)

print(account1.get_balance())

account1.set_balance(10000)
print(account1.get_balance())

account1.set_balance(-500)


# Modern Way in python using @property decorator:
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self):               # Getter
        return self.__balance

    @balance.setter
    def balance(self, amount):       # Setter
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative")


account1 = BankAccount(5000)

print(account1.balance)

account1.balance = 10000
print(account1.balance)

account1.balance = -500