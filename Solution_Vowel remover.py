def shortcut(vowels, s):
    print()
    for v in vowels:
        vowel_index = s.find(v)
        if vowel_index != -1:
            s = s.replace(s[vowel_index], "")
    print("The string without vowels is:" + '"' + str(s) + '"')


def main():
    print()
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    s = str(input("Please insert the string: "))
    shortcut(vowels, s)

main()
