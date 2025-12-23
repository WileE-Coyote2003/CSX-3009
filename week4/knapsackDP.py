#Name : Thwin Htoo Aung
#id : 6612109
#Section: 541


N,M = map(int, input().split())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

dp = [[0] * (M + 1) for _ in range(N+1)] # DP table: (N+1) x (M+1)

for i in range(N - 1, -1 , -1 ): # i decreases (N-1 → 0)
    for C in range(M+1): # C increase 0 to M+1

        skip = dp[i+1][C] # skip item i

        if w[i] <= C: # take item i
            take = v[i] + dp[i+1][C - w[i]]
        else:
            take = -1
        dp[i][C] = max(skip, take)

print(dp[0][M])