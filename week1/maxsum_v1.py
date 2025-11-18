#Name: Thwin Htoo Aung
#ID: 6612109
#Section: 541
import time
start = time.process_time()

def Sum(x, i, j):
    s = 0
    for k in range(i, j + 1):
        s += x[k]
    return s

def MaxSum(x):
    n = len(x) 
    max_sum = -float('inf')
    for i in range(n):
        for j in range(i,n):
            sum = Sum(x,i,j)
            if sum > max_sum:
                max_sum = sum
    return max_sum

x = list(map(int, input().split()))

result = MaxSum(x)
finish = time.process_time()
print("Time taken:", finish - start)