#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/10/2021
Purpose: Review the filter() function, functools
"""

from functools import reduce
import operator


# --------------------------------------------------
def main():
    """Make your noise here"""

    # Task: Create a list of all positive numbers
    numbers = [-7, 2, 5, 8, -1, 90, -2, -33, 12]

    # List Comprehension
    positives = [number for number in numbers if number >= 0]
    print(positives)

    # Generator
    positives = list((number for number in numbers if number >= 0))
    print(positives)

    # filer() and lambda
    # filter is also a lazy evaluation
    positives = list(filter(lambda x: x > 0, numbers))
    print(positives)
    # positives = filter(lambda x: x >= 0, numbers)
    print(positives)

    # a + b = operator.add(a, b)
    accumulator = operator.add(numbers[0], numbers[1])
    for item in numbers[2:]:
        accumulator = operator.add(accumulator, item)
    print(accumulator)
    # Use reduce
    print(reduce(operator.add, numbers, 0))


# --------------------------------------------------
if __name__ == '__main__':
    main()
