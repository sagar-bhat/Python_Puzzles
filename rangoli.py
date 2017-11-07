'''
Program for Printing Rangoli
of a given Length or Size
Written by - Sagar Bhat

'''

import sys


def pattern(i, j, prev):
    '''
    Prints individual character in a row
    '''
    if (j >= len - i + 1) and (j <= len + i - 1):
        sys.stdout.write("-{0}".format(chr(prev)))
        if j < len:
            prev = prev - 1
        else:
            prev = prev + 1
    else:
        sys.stdout.write("--")
    return prev

if __name__ == "__main__":

    len = int(raw_input("Enter the size of Rangoli: "))
    # val represents character value
    val = len + 96
    prev = val

    # Prints the Top Half of the Rangoli
    for i in range(1, len + 1):
        for j in range(1, 2 * len):
            prev = pattern(i, j, prev)
        prev = val
        print ""

    # Prints the Bottom Half of the Rangoli
    for i in reversed(range(1, len)):
        for j in range(1, 2 * len):
            prev = pattern(i, j, prev)
        prev = val
        print ""

