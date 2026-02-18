#Name : Thwin Htoo Aung
#id : 6612109
#Section: 541
import sys
sys.setrecursionlimit(10000)

N,M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

x = [0]*N # [0,0,0,0,0]
call_count = 0

def comb(i):
    global call_count
    call_count += 1
    if i == N:
        sw = sv = 0
        for j in range(N):
            if x[j] == 1: # first x[0]
                sw += w[j] # sum of w[j] in the range N
                sv += v[j] # 
        if sw > M:
            return - 1
        else:
            return sv

    # Try selecting item i ( include )
    x[i] = 1
    a = comb(i + 1) #[1,0,0,0,0] ,[1,1,0,0,0] ,[1,1,1,0,0] ,[1,1,1,1,0], [1,1,1,1,1]

    # Try not selecting item i ( exclude )
    x[i] = 0
    b = comb(i + 1) # [1,1,1,1,0] at combo (4 + 1)

    return max(a, b)


# run Version 1
ans = comb(0)
print(ans)
print("Recursive call_count:",call_count)
