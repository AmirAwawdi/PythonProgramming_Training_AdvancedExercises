import math
# import numpy as np
# import matplotlib as mtl
# import pandas as pd
# import re
# from num2words import num2words


def prime_check(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def prime_list(num):
    primes = []
    n = 3
    while n < num:
        if prime_check(n):
            primes.append(n)
        n += 2
    return primes


def odd_check(num):
    if num <= 1:
        return False
    if num % 2 != 0:
        return True
    else:
        return False


def goldbach_conjecture_check(num):
    primes_smaller_num = prime_list(num)
    i = 0
    while not odd_check(num - primes_smaller_num[i]):
        if (math.sqrt((num - primes_smaller_num[i]) / 2)).is_integer():
            return True
        else:
            i += 1
            if i == len(primes_smaller_num):
                return False


def main():
    goldbach_odd_composite = []
    num = 9
    while goldbach_conjecture_check(num):
        print(num)
        goldbach_odd_composite.append(num)
        num += 2
        while prime_check(num):
            num += 2
    goldbach_odd_composite.append(num)
    print("The smallest odd composite that breaks Goldbach’s conjecture is:  " + str(goldbach_odd_composite[-1]))



main()
