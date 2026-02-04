""" Creating simple bank account class """

class account:
    def __init__(self,bal,acc):
        self.balance= bal
        self.account_no= acc
    
    def debit(self,amount):           # Debit method
        self.balance -= amount
        print("Rs",amount, "was debited:")
        print("Total balance:",self.get_balance())

    def credit(self,amount):        # credit method
        self.balance += amount
        print("Rs",amount,"was credited:")
        print("Total balance:",self.get_balance())

    def get_balance(self):                         # Balance method
        return self.balance
    
a1 = account(1000,1234)
m = int(input("Enter the amount you want to debit:"))    #Taking debit amount input from user
a1.debit(m)
n = int(input("Enter the amount you want to credit:"))   #Taking credit amount input from user
a1.credit(n)