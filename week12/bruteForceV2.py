#Name : Thwin Htoo Aung
#id : 6612109
#Section: 541
import sys
sys.setrecursionlimit(10000)

N,M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

call_count = 0

#with two state varaiable 
def maxVal(i,C):
    global call_count
    call_count += 1
    if i == N:
        return 0 
    else:
        skip = maxVal(i+1,C)
        if w[i] <= C:
            take = v[i] + maxVal(i+1,C-w[i])
        else:
            take = -1 
        return max(skip, take)
    
result = maxVal(0,M)
print(result)
print("Recursive call_count:",call_count)
