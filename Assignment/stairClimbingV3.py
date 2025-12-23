#Name : Thwin Htoo Aung
#Id : 6612109
#Section : 541
def min_energy_dp(cost):
    n = len(cost)

    # DP array
    dp = [0] * n

    # Base cases
    dp[0] = cost[0]
    dp[1] = cost[1]

    # Fill DP table
    for i in range(2, n):
        dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

    # Final answer
    return min(dp[n - 1], dp[n - 2])


# Example usage
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

print("Minimum energy (Dynamic Programming):", min_energy_dp(cost))