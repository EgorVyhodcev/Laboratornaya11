#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiplication():
    mp = 1
    a = int(input("Enter the number: "))
    while a != 0:
        mp *= a
        a = int(input("Enter the number: "))
    return mp


if __name__ == '__main__':
    print(f"The multiplication of entered numbers is: {multiplication()}")
