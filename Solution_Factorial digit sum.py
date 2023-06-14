import math

def input_number():
    number = int(input("Please enter factorial number: "))
    return number

def sum_digits(n):
    n_mod = divmod(n, 10)
    sum_n = 0
    while n_mod[0] != 0:
        sum_n = n_mod[1] + sum_n
        n_mod = divmod(n_mod[0], 10)
    sum_n = n_mod[1] + sum_n
    return sum_n


def main():
    n = math.factorial(input_number())
    print(n)
    print(sum_digits(n))


main()

