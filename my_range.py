#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""


# --------------------------------------------------
def main():
    """Review ranges"""
    r = range(5)
    print(r)
    for item in r:
        print(item)

    # Set the upper and lower limit
    r = range(5, 10)
    for item in r:
        print(item)

    # Create list out of ranges
    l = list(range(50, 55))
    print(l)
    print(type(l))
    for item in l:
        print(item)

    # Create list out of multiple ranges
    # Ranges third optional parameter is the step size
    l = list(range(0, 10, 2)) + list(range(20, 60, 3))
    print(l)

    # Enumerate
    t = [6, 345, 67, 1, 99, 234]
    for i, v in enumerate(t):
        print(f'Index {i}, value {v}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
