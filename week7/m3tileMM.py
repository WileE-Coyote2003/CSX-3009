# Name : Thwin Htoo Aung
# Id : 6612109
# Section: 541

import sys
sys.setrecursionlimit(10001)

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

memo = [[-1]*3 for _ in range(L+1)]

def nWays(d, s):
    if memo[d][s] != -1:
        return memo[d][s]

    if d == L:
        memo[d][s] = 1 if s == FLAT else 0
        return memo[d][s]

    counter = 0

    if s == FLAT:
        counter += nWays(d + 1, UPPER2)
        counter += nWays(d + 1, LOWER2)
        if d + 2 <= L:
            counter += nWays(d + 2, FLAT)
    else:
        counter += nWays(d + 1, FLAT)
        if d + 2 <= L:
            counter += nWays(d + 2, s)

    memo[d][s] = counter
    return memo[d][s]

print(nWays(0, FLAT))