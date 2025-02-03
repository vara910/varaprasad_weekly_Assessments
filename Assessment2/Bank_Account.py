class BankAccount:
    def __init__(self):
        self.balance = 0  

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"{amount} has been deposited.")
            print(f"Current balance:{self.balance}")
        else:
            print("enter the correct ammount to be deposited")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance ")
        elif amount > 0:
            self.balance -= amount
            print(f"{amount} has been withdrawn")
            
        else:
            print("Invalid withdrawal amount.")

    def display(self):
        print(f"Current account balance: {self.balance}")
bank = BankAccount()
bank.deposit()
bank.withdraw()
bank.display()
