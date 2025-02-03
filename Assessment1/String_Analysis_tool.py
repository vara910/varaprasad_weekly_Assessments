# User input string 
user_string = input("Enter a string: ")

def analyze_string(default_string):
    vowels = "aeiouAEIOU"
    digits = "0123456789"
    
    vowel_count = consonant_count = digit_count = special_count = 0
    
    for char in default_string:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():  # If it's a letter but not a vowel, it's a consonant
            consonant_count += 1
        elif char in digits:
            digit_count += 1
        else:
            special_count += 1  # Special characters (spaces, punctuation, etc.)
    
    # Reverse the string
    reversed_string = default_string[::-1]
    
    #Printing the count of each item
    print(f"Vowels: {vowel_count}")
    print(f"Consonents: {consonant_count}")
    print(f"Digits: {digit_count}")
    print(f"Special symbols: {special_count}")
    print(f"Reversed string: {reversed_string}")

analyze_string(user_string)