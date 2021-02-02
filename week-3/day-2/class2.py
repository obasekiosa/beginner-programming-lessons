
class A():
    def printname(self):
        print("A")

class Operator(A):

    def printname(self):
        print("OP")



class Account(A):

    def __init__(self, initialBalance=0):
        self.initialBalance = initialBalance
        self.balance = initialBalance
    
    def __str__(self):
        return f"Your account balance is {self.initialBalance}"

    def add(self, value):
        self.balance += value

    def __repr__(self):
        return f"Account(balance = {self.initialBalance}"

    def __le__(self, value):
        return super().__le__(value)


    def __eq__(self, value):
        
        return self.balance == value.balance

    # def printname(self):
    #     print("acc")


    def printAccountBalance(self):
        print(self.initialBalance)

class SpecialAccocunt(Account, Operator):

    def __init__(self, initialBalance=78, specialBalance = 45):
        
        self.specialBalance = specialBalance
        # super().__init__(initialBalance=initialBalance)

    def printBalace(self):
        print(self.initialBalance)
        # print(self.specialBalance)


acount = Account(1000)


s_acount = SpecialAccocunt()
s_acount.printname()

