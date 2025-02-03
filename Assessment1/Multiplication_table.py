# Get input from the user to get the multiplication table
number = int(input("Enter the number for the multiplication table: "))
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

# Calculate the multiplication table for the input values
def generate_multiplication_table(number, start, end):
    for i in range(start, end + 1):
        print(f"{number} x {i} = {number * i}")

# Generate and display the multiplication table
def main():
    generate_multiplication_table(number, start, end)
main()
