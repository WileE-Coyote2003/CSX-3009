#Name : Thwin Htoo Aung
#ID : 6612109
#Section : 541
# Rod Cutting Problem without memoization - Recursive Approach
import time
call_count = 0
prices = list(map(int, input().split()))

start = time.process_time()

def MaxRevenue(l,prices):
    global call_count
    call_count += 1
    if l == 0:
        return 0
    
    best = 0
    for i in range(1,l+1): #starting with 1 cut from length l to l cuts
        best = max(best, prices[i-1] + MaxRevenue(l - i, prices))
    return best

print("Maximum Revenue:", MaxRevenue(10, prices))
print("Function call count:", call_count)
finish = time.process_time()
print("Time taken:", finish - start)