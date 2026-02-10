#Name: Thwin Htoo Aung
#ID: 6612109
#Section: 541
#Divide and Conquer V2
a, x = map(int, input().split())

MOD = 2147483647

def fast_pow(a, x):
    if x == 0:
        return 1
    if x == 1:
        return a % MOD

    half = fast_pow(a, x // 2)          # keep x integer using //
    half = (half * half) % MOD          # (a^(x//2))^2

    if x % 2 == 1:                      # if x is odd, multiply by a once more
        half = (half * (a % MOD)) % MOD

    return half

print(fast_pow(a, x))
