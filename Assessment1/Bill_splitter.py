# Input for calculating the bill and bill separation
total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage: "))

def split_bill(total_bill, num_people, tip_percentage):
    # Calculate the tip amount
    tip_amount = (tip_percentage / 100) * total_bill
    # Calculate the total amount including the tip
    total_amount = total_bill + tip_amount
    # Calculate the amount each person needs to pay
    amount_per_person = total_amount / num_people
    return amount_per_person

 # Calculate and display the amount each person has to pay
def main():
    amount = split_bill(total_bill, num_people, tip_percentage)
    print(f"Each person has to pay: {amount:.2f}")

main()
