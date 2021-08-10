#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/10/2021
Purpose: Review the map() function
"""


# --------------------------------------------------
def combine(size, color, animal):
    return f'{size} {color} {animal}'


# --------------------------------------------------
def main():
    """Make your noise here"""
    # Map() is lazy. It only produces the values as they are needed
    # ord: unicode value
    m = map(ord, 'The purple Weber State')
    print(m)
    print(next(m))     # one at a time, "on demand"
    print(next(m))
    print(next(m))
    # print(list(m))   # all elements
    print(list(map(ord, 'The purple Weber State')))
    # or use loop
    for o in map(ord, 'The purple Weber State'):
        print(o)

    # Multiple mapping
    sizes = ['small', 'medium', 'large']
    colors = ['green', 'blue', 'red']
    animals = ['cow', 'dog', 'cat']
    # Create a list from a map
    print(list(map(combine, sizes, colors, animals)))

# --------------------------------------------------
if __name__ == '__main__':
    main()