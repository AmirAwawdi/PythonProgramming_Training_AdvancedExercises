
## Help by ChatGBT

def romanize(number):
    # This is a 'dict' object = a dictionary in Python that maps integer values to their corresponding
    # Roman numeral string representation.
    roman_numeral_map = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }
    roman_numeral = ""
    for value, letter in roman_numeral_map.items():
        roman_numeral += letter * (number // value)
        number = number % value
    return roman_numeral


def main():
    number = int(input("Please enter a positive integer: "))
    # an instance of a class is also called an object
    # 'isinstance' is a built-in function in Python that checks if an object is an instance of a specified
    # class or of a subclass thereof
    # The function returns True if the object is an instance of the 'classinfo' or a subclass thereof,
    # and False otherwise.
    # raise is a keyword in Python used to raise an exception. It is used to interrupt the normal
    # flow of a program when some error occurs and to provide a more informative error message to the user.
    if not isinstance(number, int) or number <= 0:
        raise ValueError("Input must be a positive integer between 1 and 3999")
    print("Romnized: " + str(romanize(number)))


main()

##########################

#  For SandBox

# def romanize(number):
#     roman_numeral_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"),
#                          (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
#
#     roman_numeral = ""
#     for value, letter in roman_numeral_map:
#         roman_numeral += letter * (number // value)
#         number = number % value
#     return roman_numeral
#
#
# def main():
#     number = int(input("Please enter a positive integer: "))
#     print("Integer: " + str(number))
#     print("Romnized: " + str(romanize(number)))
#
#
# main()
