import math
import numpy as np
import matplotlib as mtl
import pandas as pd
import re
from num2words import num2words


def input_number():
    n1 = int(input("Please enter the lower limit number: "))
    n2 = int(input("Please enter the upper limit number: "))
    numbers_list = []
    for i in range(n2-n1+1):
        numbers_list.append(n1+i)
    return numbers_list


def numbers_to_letters(numbers_list):
    words_list = []
    for i in range(len(numbers_list)):
        words_list.append(num2words(numbers_list[i]))
    return words_list


def count_letters(words_list):
    sum_len = 0
    for j in range(len(words_list)):
        split_words_list = re.split(', |-| ', words_list[j])
        for k in range(len(split_words_list)):
            sum_len = sum_len + len(split_words_list[k])
    return sum_len


def main():
    numbers_list = input_number()
    words_list = numbers_to_letters(numbers_list)
    print(count_letters(words_list))


main()
