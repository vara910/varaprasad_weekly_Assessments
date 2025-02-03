# Random is a class that generates a random number 
import random

num=int(input("Enter your guess: "))

def guess_num(num):
    computer1= random.randrange(1,100)
    for i in range(num):
        if num > computer1:
            print("Too high !!")
        else:
            print("Too low")

def main():
    guess_num(computer1)
main()