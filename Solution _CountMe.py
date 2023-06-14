def count_nine(n):
    counter = 0
    for j in range(n+1):
        for i in range(len(str(j))):
            digits = divmod(j, 10)
            j = digits[0]
            if digits[1] == 9:
                counter += 1
    print("When counting from 1 to " + str(n) + " the digit 9 will be used " + str(counter) + " times")

def main():
    number = int(input("Please enter and integer: "))
    count_nine(number)


main()

#
# i=9015
# print(len(str(i)))
# print(divmod(i,10))
# a=divmod(i,10)
# print(divmod(a[0],10))