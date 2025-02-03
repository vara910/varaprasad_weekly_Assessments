deposit = int(input("Enter your deposit value: "))
withdrawal= int(input("Enter your withdrawal amount: "))
account_balance= 0

def deposit_amount(deposit,account_balance):
    account_balance+= deposit
    return account_balance

def withdraw_amount(account_balance, withdrawal):
    if account_balance>= withdrawal:
        account_balance -=  withdrawal
    else:
        print("Insufficent balance")
    return account_balance
    
def check_balance(account_balance):
    return account_balance

def main():
    global account_balance
    account_balance = deposit_amount(deposit, account_balance)  # Deposit the amount
    account_balance = withdraw_amount(account_balance, withdrawal)  # Withdraw the amount
    print("Current account balance:", check_balance(account_balance))  # Check and print the balance
main()


