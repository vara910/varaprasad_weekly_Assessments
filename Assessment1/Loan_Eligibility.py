salary= int(input("Enter your salary: "))
age= int(input("Enter your age: "))
credit_score=int(input("Enter your credit score: "))

def loan_eligibility(salary, credit_score):
    if age < 21:
        return
    elif age > 21 and salary > 20000 and credit_score > 600:
        print("Congratulations, your loan is approved !! You may proceed with the procedure. ")
    elif salary <= 20000 and credit_score < 600:
        print("Your loan is rejected as your salary and credit score are below the eligibility criteria. ")
    elif salary >20000 and credit_score < 600:
        print("Your loan is rejected as your credit score didn't meet the minimum score.")
    elif salary < 20000 and credit_score > 600:
        print("Your loan is rejected as your salary didn't meet the minimum cut-off. ")
    else:
        print("Not eligible")

def main():
    loan_eligibility(salary, credit_score)
main()