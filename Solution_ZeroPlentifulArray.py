def is_zero_plentiful(values):
    n_multiple_zeros = 0
    zero_counter = 0
    loop_counter = 0
    for i in values:
        loop_counter += 1
        if i != 0:
            if zero_counter >= 4:
                n_multiple_zeros += 1
            else:
                n_multiple_zeros = 0
            zero_counter = 0
        else:
            zero_counter += 1
            if loop_counter == (len(values)):
                if zero_counter >= 4:
                    n_multiple_zeros += 1
                else:
                    n_multiple_zeros = 0
    return n_multiple_zeros


def main():
    print("Enter a list of integers according the pattern [#1, #2, ...]")
    # values = [0, 0, 0, 0, 1, 0, 0, 0, 0]
    # values = [0, 0, 0, 0, 0, 1]
    # values = [0, 0, 0, 0, 1, 0]
    # values = [0, 0, 0, 1, 0, 0]
    # values = [1, 2, 3, 4, 5]
    # values = []
    values = [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
    print("The list you entered: ")
    print(values)
    num_zero = is_zero_plentiful(values)
    print("This list contains " + str(num_zero) + " long sequences of zeros as requested")


main()
