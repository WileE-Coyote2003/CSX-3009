# Name : Thwin Htoo Aung
# ID : 6612109
# Section : 541
# Minimum Coin Change with memoization - Recursive Approach

import time
import math
import sys
sys.setrecursionlimit(10000)

denomiator = list(map(int, input().split()))
amount_of_change = int(input())

start = time.process_time()

def min_change(n, Coins, memo):
    if n == 0:
        memo[n] = 0
        return 0

    if n in memo:
        return memo[n]

    v = math.inf
    for c in Coins:
        if c <= n:
            v = min(min_change(n - c, Coins, memo) + 1, v)

    memo[n] = v
    return v


memo = {}
result = min_change(amount_of_change, denomiator, memo)
print(result)
finish = time.process_time()
print("Time taken:", finish - start)
