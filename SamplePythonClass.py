class BankAccount:
    "This class reprents a bank account"

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise InsufficientFundsException("Insufficent balance")

####################### Testing above class #############################

# Create a bank account object
account = BankAccount(8797998, 10000)

# Make a deposti
account.deposit(50)

# Try to make a withdrawl
try:
    account.withdraw(1000)
except InsufficientFundsException as e:
    print("Error:", e)
else:
    print("Withdrawl sucessful")


# Print the current balance
print("Current balance: ", account.balance)
#########################################################################