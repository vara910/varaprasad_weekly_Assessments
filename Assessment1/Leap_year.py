def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    while True:
        year = int(input("Enter a year to check if it is a leap year (or enter 0 to exit): "))
        if year == 0:
            print("Exiting the program.")
            break  
        if is_leap_year(year):
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year.")

main()
