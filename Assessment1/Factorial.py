# Input number for factorial calculation
num = int(input("Enter a number: "))

def factorial(n):
    if n < 0:
        return "Invalid" 
    
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i  
    return factorial

# Calculate and display the factorial
res= factorial(num)
print(f"Factorial of the num is: {res}")