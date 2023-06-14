def max_min_max(values):
    if len(values) == 1:
        print("There is only one value in the list !")
        print("Please enter a list containing 3 or more values.")
        return 0
    if len(values) == 2:
        print("There are only two values in the list.")
        print(sorted(values))
        return 0
    else:
        sorted_values = sorted(values)
        minvalue = sorted_values[0]
        maxvalue = sorted_values[len(sorted_values) - 1]
        count = 1
        for count in range(len(sorted_values) - 2):
            i = count
            while int(maxvalue - i) != sorted_values[len(sorted_values)-1 - i]:
                i += 1
                if i == len(sorted_values):
                    print([minvalue, int(maxvalue - count), maxvalue])
                    return 0
            if count == len(sorted_values)-1:
                print("There isn't a maximum absent values")
                print([minvalue, maxvalue])
                return 0



def main():
    print("Enter a list of integers according the pattern [#1, #2, ...]")
    # values = [1, 234, 3456, 467, 67, -1, -34, -34534, -23]
    values = [1, 1000, 4999, 500, 5000, 600, 100]
    print("The list you entered: ")
    print(values)
    print("Results:")
    max_min_max(values)

main()
