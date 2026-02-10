#Name: Thwin Htoo Aung
#ID: 6612109
#Section: 541
#Divide and Conquer
a, x = map(int, input().split())

MOD = 2147483647

result = 1
for _ in range(x):
    result = (result * a) % MOD

print(result)