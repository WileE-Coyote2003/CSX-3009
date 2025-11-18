#Name: Thwin Htoo Aung
#ID: 6612109
#Section: 541
import sys
sys.setrecursionlimit(100000)

n = int(input())

x = [0] * n
def combination(i):
    
    if i == n: # Once i is equal to the length of array generate arrray's elements
        print(*x)
        return
    
    x[i] = 0 
    #recursive call
    combination(i + 1)

    x[i] = 1
    combination(i + 1)

combination(0)

