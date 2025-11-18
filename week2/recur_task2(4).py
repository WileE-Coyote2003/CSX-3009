#Name: Thwin Htoo Aung
#ID: 6612109
#Section: 541
import sys
sys.setrecursionlimit(100000)

n = int(input("Enter n: "))
k = int(input("Enter k (0 <= k <= n ): "))

x = [0] * n
def combination(i):
    if i == n:
        if x.count(1) == k: #count number of 1 at each element inside arrry and equal with k
            print(*x)
            return 1
        else:
            return 0
    
    x[i] = 0
    first_rec_call = combination(i + 1)

    x[i] = 1
    second_rec_call = combination(i + 1)
    return first_rec_call + second_rec_call

total = combination(0)
print("Total combinations with exactly", k, "ones:", total)

