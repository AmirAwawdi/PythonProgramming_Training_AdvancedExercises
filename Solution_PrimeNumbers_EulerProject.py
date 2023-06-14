import math


def prime_check(num):
    if num <= 1:
        return False
    # The upper bound of the range is the integer part of the square root of num plus 1. This is because a number n is
    # only divisible by numbers less than or equal to sqrt(n).
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    # False mean the num is not a prime number
    return True


def prime_list(n):
    primes = []
    num = 2
    while len(primes) < n:
        if prime_check(num):
            primes.append(num)
        num += 1
    print(primes)
    return primes[-1]


def main():
    n = int(input("Please enter the prime number's position: "))
    print("The " + str(n) + "# prime number is: " + str(prime_list(n)))


main()

