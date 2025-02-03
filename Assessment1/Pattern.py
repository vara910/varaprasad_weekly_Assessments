# Input value to generate a pattern 
n = int(input("Enter the number of rows: "))
def pattern(n, reverse=False):
    if reverse:
        for i in range(n, 0, -1):
            print("*" * i)
    else:
        for i in range(1, n + 1):
            print("*" * i)
reverse = input("Do you want the reverse pattern? (yes/no): ").strip().lower() == "yes"

# Generate pattern
pattern(n, reverse)
