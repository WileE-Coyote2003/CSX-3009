# Name : Thwin Htoo Aung
# ID : 6612109
# Section : 541
# Minimum Coin Change - Non-Recursive Dynamic Programming Approach

import time
import math

# Input
denominator = list(map(int, input().split()))
amount_of_change = int(input())

start = time.process_time()

# dp[v] = minimum number of coins needed to make amount v
dp = [math.inf] * (amount_of_change + 1)
dp[0] = 0   # Base case: 0 coins needed to make 0 amount

# Build the dp table from 1 → amount_of_change
for v in range(1, amount_of_change + 1):        # iterate mm’s indices
    for c in denominator:                       # try each coin
        if c <= v:
            dp[v] = min(dp[v], 1 + dp[v - c])   # compute mm[v]

result = dp[amount_of_change]

# Output
print(result)

finish = time.process_time()
print("Time taken:", finish - start)