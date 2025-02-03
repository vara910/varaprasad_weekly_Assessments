def is_palindrome(value):
    value = str(value)  # Convert number to string if needed
    return value == value[::-1]  # Check if the string is equal to its reverse

while True:
    user_input = input("Enter a string or number (or type 'exit' to quit): ")
    
    if user_input.lower() == 'exit':  # Exit condition
        print("Goodbye!")
        break
    
    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")
