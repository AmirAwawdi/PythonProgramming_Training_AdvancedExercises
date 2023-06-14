def repeat(n, s):
    new_s = str(n*s)
    print('"' + new_s + '"')


def main():
    print()
    n = int(input("Please insert an integer of how many times you want to repeat the string: "))
    print()
    s = str(input("Please insert the string: "))
    repeat(n, s)


main()
