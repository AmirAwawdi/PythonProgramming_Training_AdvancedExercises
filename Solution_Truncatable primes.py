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


def is_left_truncatable(n):
    """Check if a number is left-truncatable"""
    s = str(n)
    while s:
        if not prime_check(int(s)):
            return False
        s = s[1:]
    return True


def is_right_truncatable(n):
    """Check if a number is right-truncatable"""
    s = str(n)
    while s:
        if not prime_check(int(s)):
            return False
        s = s[:-1]
    return True


def main():
    truncatable_primes = []
    truncatable_primes_sum = 0
    n = 10
    while len(truncatable_primes) < 11:
        if is_left_truncatable(n) and is_right_truncatable(n):
            truncatable_primes.append(n)
        n += 1
    print("A list of the 11 truncatable primes: " + str(truncatable_primes))
    for p in truncatable_primes:
        truncatable_primes_sum = truncatable_primes_sum + p
    print("Their sum is: "+ str(truncatable_primes_sum))


main()
