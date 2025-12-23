#Name : Thwin Htoo Aung
#Id : 6612109
#Section : 541
def min_energy_bruteforce(cost, i):
    # Base cases
    if i < 0:
        return 0
    if i == 0 or i == 1:
        return cost[i]

    # Recursive case
    return cost[i] + min(
        min_energy_bruteforce(cost, i - 1),
        min_energy_bruteforce(cost, i - 2)
    )


# Example usage
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
n = len(cost)

answer = min(
    min_energy_bruteforce(cost, n - 1),
    min_energy_bruteforce(cost, n - 2)
)

print("Minimum energy (Brute Force):", answer)