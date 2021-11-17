#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def circle(radius):
    circle_square = math.pi * radius ** 2
    return circle_square


def cylinder():
    radius = float(input("Enter the radius of the cylinder: "))
    height = float(input("Enter the height if the cylinder: "))
    print("Do you want to compute the full cylinder square?")
    command = input().lower()
    if command == 'yes':
        print(2 * math.pi * radius * height + 2 * circle(radius))
    if command == 'no':
        print(2 * math.pi * radius * height)


if __name__ == '__main__':
    cylinder()
