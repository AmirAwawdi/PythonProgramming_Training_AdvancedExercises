def is_palindrome(s):
    count = len(s)
    s = s.lower()
    c = 0
    if count > 1:
        for c in range(len(s)):
            if s[c] == s[count-1]:
                count -= 1
                if count == 0:
                    return print("True")
            else:
                return print("False")
    if count == 1:
        print("True, it's a one letter string !")
    else:
        print("This isn't a valid string !")
        main()

def main():
    print()
    s = str(input("Please type a string: "))
    if s.strip().isdigit():
        print()
        print("Your input was a number")
        main()
    else:
        is_palindrome(s)


main()
