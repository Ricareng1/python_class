#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/9/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',  # One or more arguments
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items',
                        default=0)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""

    args = get_args()
    items = args.item
    number_of_items = len(items)
    bringing = ''

    # TODO: check if the list needs to be sorted

    # TODO: prepare list to print
    # 1 Item, just print it
    if number_of_items == 1:
        bringing = items[0]

    # 2 Items: item1 and item2
    elif number_of_items == 2:
       bringing = ' and '.join(items)

    # 3 or more Items: item1, item2, itemX, and itemLast
    else:
        bringing = ', '.join(items)

    # Print info
    print(f'You are bringing {bringing}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
