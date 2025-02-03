password= input("Password: ")

def strength_of_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    if not any(char.isupper() for char in password):
        return "Password must contain at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Password must contain at least one lowercase letter."
    
    if not any(char.isdigit() for char in password):
        return "Password must contain at least one digit."
    
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    if not any(char in special_characters for char in password):
        return "Password must contain at least one special character."
    
    return "Password is strong!"

# Check the strength of the password
result = strength_of_password(password)
print(result)
