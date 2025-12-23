#Name : Thwin Htoo Aung
#Id : 6612109
#Section : 541
def min_energy_memo(cost, i, memo):
    # Base cases
    if i < 0:
        return 0
    if i == 0 or i == 1:
        return cost[i]

    # If already computed, return it
    if i in memo:
        return memo[i]

    # Compute and store result
    memo[i] = cost[i] + min(
        min_energy_memo(cost, i - 1, memo),
        min_energy_memo(cost, i - 2, memo)
    )

    return memo[i]


# Example usage
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
n = len(cost)
memo = {}

answer = min(
    min_energy_memo(cost, n - 1, memo),
    min_energy_memo(cost, n - 2, memo)
)

print("Minimum energy (Memoization):", answer)