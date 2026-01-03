#Name: Thwin Htoo Aung
#ID: 6612109
#Section: 541
import sys
sys.setrecursionlimit(100000)

n = int(input("Enter n: "))

x = [0] * n
def combination(i):
    if i == n:
        #print(*x)
        return 1
    
    x[i] = 0
    first_rec_call = combination(i + 1)
    x[i] = 1
    second_rec_call = combination(i + 1)
    return first_rec_call + second_rec_call

total = combination(0)
print("Number of Combinations: ",total)

