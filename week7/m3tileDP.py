# Name : Thwin Htoo Aung
# Id : 6612109
# Section: 541

FLAT = 0
UPPER2 = 1
LOWER2 = 2

L = int(input())

dp = [[0] * 3 for _ in range(L + 2)]

# Base case
dp[L][FLAT] = 1
dp[L][UPPER2] = 0
dp[L][LOWER2] = 0

for d in range(L - 1, -1, -1):
    # FLAT state
    dp[d][FLAT] = dp[d + 1][UPPER2] + dp[d + 1][LOWER2]
    if d + 2 <= L:
        dp[d][FLAT] += dp[d + 2][FLAT]

    # UPPER2 state
    dp[d][UPPER2] = dp[d + 1][FLAT]
    if d + 2 <= L:
        dp[d][UPPER2] += dp[d + 2][UPPER2]

    # LOWER2 state
    dp[d][LOWER2] = dp[d + 1][FLAT]
    if d + 2 <= L:
        dp[d][LOWER2] += dp[d + 2][LOWER2]

print(dp[0][FLAT])