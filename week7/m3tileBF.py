# Name : Thwin Htoo Aung
# Id : 6612109
# Section: 541

import sys
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

def nWays(d, s):
    if d == L:
        if s == FLAT:
            return 1
        else:
            return 0
    counter = 0

    if s == FLAT:
        counter += nWays(d + 1, UPPER2)
        counter += nWays(d + 1, LOWER2)
        if d + 2 <= L:
            counter += nWays(d + 2, FLAT)
    else:
        counter += nWays(d + 1, FLAT)
        if d + 2 <= L:
            counter += nWays(d + 2, s) #s is either UPPER or LOWER

    return counter

print(nWays(0, FLAT))