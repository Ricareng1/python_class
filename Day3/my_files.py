#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/11/2021
Purpose: Working with files
"""

import sys


# --------------------------------------------------
def main():
    """Make your noise here"""
    print(sys.getdefaultencoding())

    # Writing text files
    f = open('wasteland.txt', mode='wt', encoding='utf-8')
    f.write('This is the first line of text I have here.')
    f.write('But, I can write more lines if I need to\n')
    f.close()

    # Reading Files
    g = open('wasteland.txt', mode='rt', encoding='utf-8')
    info = g.read(27)  # read 27 bytes
    print(info)
    info = g.read()  # read the rest
    print(info)
    g.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
