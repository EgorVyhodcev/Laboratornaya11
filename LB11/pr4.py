#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    a = input("Enter the number: ")
    return a


def test_input(a):
    return a.isdigit()


def str_to_int(a):
    a = int(a)
    return a


def print_int(a):
    print(a)


if __name__ == '__main__':
    num_str = get_input()
    if test_input(num_str):
        num = str_to_int(num_str)
        print_int(num)
    else:
        print(f"The input {num_str} is not numerical")
