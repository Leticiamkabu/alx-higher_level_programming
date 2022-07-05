#!/usr/bin/python3
def print_reversed_integer(my_list=[]):
    if my_list:
        turn = my_list.reverse()
        for i in range(len(turn)):
            print("{:d}".format(turn[i]))
