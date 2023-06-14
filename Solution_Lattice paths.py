# To reach the bottom right corner in nxn grid we need to move exactly n moves in both x and y directions
# Therefore the number of different routes equals the number of different ways
# to choose n form 2*n (n moves in both x and y directions)

def binom_coeff(n, k):
    # How many different ways to choose k from n
    numerator = 1
    denominator = 1
    for i in range(1, k+1):
        numerator *= n-k+i
        denominator *= i
    return numerator // denominator


def main():
    n = int(input("Please enter the grid's dimensions, n =  "))
    print("Starting from the upper left corner of a " + str(n) + "x" + str(n) + " grid, there are "
          + str(binom_coeff(2*n, n)) + " different routes to reach the bottom right corner")


main()
