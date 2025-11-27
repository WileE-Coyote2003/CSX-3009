# Name : Thwin Htoo Aung
# ID : 6612109
# Section : 541
# Rod Cutting Problem with memoization - Recursive Approach

import time
call_count = 0
prices = list(map(int, input().split()))

start = time.process_time()

memo = {}   # dictionary for memoization

def MaxRevenue(l, prices):
    global call_count
    call_count += 1

    # If value already computed → return from memo
    if l in memo:
        return memo[l]

    if l == 0:
        return 0

    best = 0
    for i in range(1, l + 1):
        best = max(best, prices[i - 1] + MaxRevenue(l - i, prices))

    memo[l] = best  # store in memo before returning
    return best


print("Maximum Revenue:", MaxRevenue(10, prices))
print("Function call count:", call_count)
finish = time.process_time()
print("Time taken:", finish - start)
