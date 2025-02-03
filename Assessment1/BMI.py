# User input of weight and height for BMI calculation

weight = float(input("Enter weight (kg): "))
height_cm = float(input("Enter height (cm): "))

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)  # BMI formula 

    # BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24:
        category = "Normal weight"
    elif 25 <= bmi < 29.5:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

# Calculate and print the result
bmi, category = calculate_bmi(weight, height_cm)
# print(f"\nYour BMI: {bmi:.2f}")
# print(f"Category: {category}")
print(f"Your BMI: {bmi}")
print(f"Categry: {category}")

 
