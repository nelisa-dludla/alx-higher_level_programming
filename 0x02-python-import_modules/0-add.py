#!/usr/bin/python3

'''
This script imports a function def add(a, b): from the file
add_0.py and prints the result of the addition 1 + 2 = #!/usr/bin/env python3
'''

from add_0 import add


def main():
    a = 1
    b = 2

    print('{} + {} = {}'.format(a, b, add(a, b)))


if __name__ == '__main__':
    main()
