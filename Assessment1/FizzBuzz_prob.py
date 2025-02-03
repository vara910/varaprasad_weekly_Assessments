num= int(input("Enter the num: "))

def FizzBuzz(num):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")

def main():
    FizzBuzz(num)
main()