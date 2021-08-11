#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""


def online_count(statuses):
    return len([status for status in statuses.values() if status == 'online'])


# --------------------------------------------------
def main():
    """Make your noise here"""
    statuses = {"Alice": "online",
                "Bob": "offline",
                "Eve": "online" }

    print(online_count(statuses))

# --------------------------------------------------
if __name__ == '__main__':
    main()
