#!/usr/bin/python3
if __name__ == "__main__":
    """This script imports add and uses it"""
    from add_0 import add
    a = 1
    b = 2
    sum = 0
    sum += add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))
