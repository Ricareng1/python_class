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
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Encode phone number using the Jumper Five Algorithm"""

    args = get_args()
    jumper = {'1': '9', '2': '8', '3': '7', '4': '6', '5': '0',
              '6': '4', '7': '3', '8': '2', '9': '1', '0': '5'}

    # Method 1:
    for character in args.text:
        print(jumper.get(character, character), end='')
    print()

    # Method 2:
    new_text = ''
    for character in args.text:
        new_text += jumper.get(character, character)
    print(new_text)

    # Method 3:
    new_text = []
    for character in args.text:
        new_text.append(jumper.get(character, character))
    print(''.join(new_text))

    # Method 4: List Comprehension
    print(''.join([jumper.get(character, character) for character in args.text]))


# --------------------------------------------------
if __name__ == '__main__':
    main()