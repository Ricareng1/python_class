#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""


# --------------------------------------------------
def take(count, iterable):
    """
    Take items for the from of the iterable
    :param count: The maximum number or items to retrieve
    :param iterable: The source series
    :yield: At most 'count' items for 'iterable'
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


# --------------------------------------------------
def run_take():
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


# --------------------------------------------------
def distinct(iterable):
    """
    Return unique items by eliminating duplicates
    :param iterable: The source series
    :return: Uniquie elements in order for 'iterable'
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


# --------------------------------------------------
def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


# --------------------------------------------------
def run_pipeline():
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


# --------------------------------------------------
def main():
    """Make your noise here"""
    # run_pipeline()

    # Generators: (expr(item) for item in iterable)
    # Task: Calculate the sum of the first 1 million square numbers

    # Generator (Faster)
    m_sq = (x*x for x in range(1, 1000000))
    print((type(m_sq)))

    # Comprehension
    l_sq = [x*x for x in range(1, 1000001)]
    print(f'The sum of the first 1000 square numbers is: {sum(l_sq)}')

# --------------------------------------------------
if __name__ == '__main__':
    main()
