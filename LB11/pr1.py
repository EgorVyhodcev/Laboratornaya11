#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def test():
    a = int(input("Enter the number: "))
    if a > 0:
        positive()
    elif a < 0:
        negative()


def positive():
    print("This number is positive")


def negative():
    print("This number is negative")


if __name__ == '__main__':
    test()
