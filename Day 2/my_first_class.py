#!/usr/bin/env python3
"""
Author : t18 <me@wsu.com>
Date   : 8/10/2021
Purpose: Review basics of classes
"""

from math import sqrt


class Point:
    """Represents a point in a 2-D geometric coordinates"""

    def __init__(self, x=0, y=0):
        """
        Initializes that position of a new point. If they are
        not specified, the point defaults to the origin.
        :param x: x-coordinate. Default = 0
        :param y: y-coordinate. Default = 0
        """
        self._x = x
        self._y = y

    def reset(self):
        """Resets the point to the new location in 2D space"""
        self.move(0, 0)

    def move(self, x, y):
        """
        Move point to a new location in 2D space
        :param x: x-coordinate
        :param y: y-coordinate
        :return: Nothing
        """
        self._x = x  # for "private" use _
        self._y = y

    # Task: Calculate the distance
    def calculate_distance(self, other_point):
        """
        Calculates the distance from this point to a second point
        passed as a parameter.
        This function uses the Pythagorean Theorem to calculate
        the distance between two points
        :param other_point: second object of type Point
        :return: distance between two points (float)
        """
        return sqrt(pow((other_point._x - self._x), 2) +
                    pow((other_point._y - self._y), 2))


# --------------------------------------------------
def main():
    """Make your noise here"""
    p1 = Point()
    p2 = Point(-9, 3)
    # <object>.<attribute> - <value>
    # p1._x = 5
    # p1._y = 4
    # p2._x = 3
    # p2._y = 9
    print(p1._x, p1._y)
    print(p2._x, p2._y)
    p2.reset()  # reset values
    print(p2._x, p2._y)

    p1.move(9, 9)
    print(p1._x, p1._y)

    p1.move(4, 3)
    p2.move(3, -2)

    print(p1.calculate_distance(p2))


# --------------------------------------------------
if __name__ == '__main__':
    main()
