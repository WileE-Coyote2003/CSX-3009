# Name: Thwin Htoo Aung
# ID: 6612109
# Section: 541

import time
start = time.process_time()

values = list(map(int, input().split()))
n = len(values)

best_diff = None   # store minimal difference found

# ------------------------------------------------------------
# Recursive function to generate all 2^n group assignments
# i  = current index (0…n-1)
# sum_g1 = running sum of values in Group 1
# ------------------------------------------------------------
def solve(i, sum_g1):
    global best_diff

    # Base case: all items assigned
    if i == n:
        total_sum = sum(values)         # total of all items
        sum_g0 = total_sum - sum_g1     # group 0 sum
        diff = abs(sum_g1 - sum_g0)     # difference between groups

        # update minimal difference found
        if best_diff is None or diff < best_diff:
            best_diff = diff
        return

    # --------------------------------------------------------
    # Option 1: assign item i to group 0
    # (sum_g1 does not change)
    # --------------------------------------------------------
    solve(i + 1, sum_g1)

    # --------------------------------------------------------
    # Option 2: assign item i to group 1
    # (add its value to sum_g1)
    # --------------------------------------------------------
    solve(i + 1, sum_g1 + values[i])


# Run the recursive search
solve(0, 0)

# Print minimal difference result
print(best_diff)

finish = time.process_time()
print("Time taken:", finish - start)