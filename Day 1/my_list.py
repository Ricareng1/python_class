#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""


# --------------------------------------------------
def main():
    """Review lists"""
    r = [4, -2, 10, 18, 22, 55, 2, 77]

    # Slicing
    print(r[2:6])
    print(f'Length of list: {len(r)} ')
    print(f'Last element: {r[-1]} ')

    # Copy list, by default Python uses Shallow copies
    t = r
    print(f'1. Is t the same are r? {t is r}')

    # To make a copy, generate a new list
    u = r[:]
    print(f'2. Is u the same are r? {u is r}')

    # Faster method
    v = r.copy()
    print(f'3. Is v the same are r? {v is r}')
    print(f'4. Is v equivalent as r? {v == r}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
