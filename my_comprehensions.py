#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

from math import sqrt
from pprint import pprint as pretty_print


# --------------------------------------------------
def is_prime(number):
    """
    Return true or false if the input in a primer number
    :param number: integer
    :return: True or False
    """
    if number < 2:
        return False
    for i in range(2, int(sqrt(number) )+ 1):
        if number % i == 0:
            return False
    return True


# --------------------------------------------------
def main():
    """Iterable and Comprehensions"""
    words = "Today I am very happy because Barcelona does not have Messi with them any more".split()
    print(words)

    # List Comprehension
    length_of_words = []
    for word in words:
        length_of_words.append(len(word))
    print(length_of_words)

    # List Comprehension: [expression for item in iterable]
    totals = [len(word) for word in words]
    print(totals)

    # Add a predicate to your comprehension
    prime_numbers = [x for x in range(1001) if is_prime(x)]
    print(prime_numbers)
    print(sum(prime_numbers))


# --------------------------------------------------
if __name__ == '__main__':
    main()
