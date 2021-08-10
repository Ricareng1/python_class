#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/10/2021
Purpose: Review itertools package
"""


# --------------------------------------------------
def main():
    """Make your noise here"""

    # Task: Check all member in the collection have Uppercase of the first letter
    cities = ['London', 'Madrid', 'New York', 'Ogden']
    print(f'The cities list is {all(city == city.title() for city in cities)}  to go')

    # Use built-in zip
    sunday = [12, 14, 15, 15, 17, 21, 22, 23, 22, 20, 18]
    monday = [13, 14, 14, 16, 20,21, 22, 22, 21, 19, 18, 16]

    for item in zip(sunday, monday):
        print(item)
# --------------------------------------------------
if __name__ == '__main__':
    main()
