#Name : Thwin Htoo Aung
#ID : 6612109
#Section : 541
# Minimum Coin Change without memoization - Recursive Approach
import time
denomiator = list(map(int, input().split()))
amount_of_change = int(input())

start = time.process_time()

def min_change(n, Coins):
    v = float("inf")
    if n == 0:
        return 0
    for c in Coins:
        if c <= n:
            v = min(min_change(n-c,Coins)+1,v) # pick a coin c and reduce the remaining amount by c and recursively call the function 
    return v

result = min_change(amount_of_change,denomiator)
print(result)
finish = time.process_time()
print("Time taken:", finish - start)