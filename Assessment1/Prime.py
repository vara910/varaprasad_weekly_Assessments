# Print all the primes between two numbers n and m

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_num(n,m):
    primes = []
    for num in range(n,m+ 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Input of two numbers
n = int(input("Enter the 1st num: "))
m = int(input("Enter the 2nd num: "))

# Get prime numbers in the range
primes = prime_num(n,m)

# Print the prime numbers
print("Prime numbers:", primes)
