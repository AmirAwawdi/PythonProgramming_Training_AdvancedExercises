def digital_root(n):
    digits = divmod(n, 10)
    digsum = 0
    if digits[0] == 0:
        digsum = digits[1]
        return digsum

    while digits[0] != 0:
        digsum = digits[1] + digsum
        n = digits[0]
        digits = divmod(n, 10)
    digsum = digits[1] + digsum

    digits = divmod(digsum, 10)
    if digits[0] != 0:
        digital_root(digsum)
    else:
        print("Its digital root is: " + str(digsum))


def main():
    n = int(input("Please enter and integer: "))
    digital_root(n)


main()

