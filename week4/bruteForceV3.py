#Name : Thwin Htoo Aung
#id : 6612109
#Section: 543
import sys
sys.setrecursionlimit(10000)

N,M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

call_count = 0
memo = {} # dictionary for memoization

#with two state varaiable 
def maxVal(i,C):
    global call_count
    call_count += 1

    # If value already computed → return from memo
    key = (i,C)
    if key in memo:
        return memo[key]
    
    if i == N:
        memo[key] = 0
        return 0 
    else:
        skip = maxVal(i+1,C)
        if w[i] <= C:
            take = v[i] + maxVal(i+1,C-w[i])
        else:
            take = -1 
        result = max(skip, take)

        memo[key] = result # store in memo before returning
        return result
    
result = maxVal(0,M)
print(result)
print(call_count)
