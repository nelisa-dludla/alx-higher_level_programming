#!/usr/bin/python3
'''
Function divides element by element 2 lists
'''


def list_division(my_list_1, my_list_2, list_length):
    newList = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            result = 0
            print('wrong type')
        except ZeroDivisionError:
            result = 0
            print('division by 0')
        except IndexError:
            result = 0
            print('out of range')
        finally:
            newList.append(result)

    return newList
