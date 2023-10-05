#!/usr/bin/python3
if __name__ == "__main__":
    """
    This script imports a function def add(a, b): from the file
    add_0.py and prints the result of the addition 1 + 2 = 3
    """
    from add_0 import add
    a = 1
    b = 2
    sum = 0
    sum += add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, sum))
