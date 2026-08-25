class Bank:
    def __init__(self,balance):
        self.__balance = balance
    def Credit(self,amount):
        self.__balance += amount
    def Debit(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")
    def display(self):
        print("Balance:",self.__balance)
bank = Bank(1000)
bank.Credit(500)
bank.Debit(200)
bank.display()
