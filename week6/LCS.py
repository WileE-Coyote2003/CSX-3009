N,M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
#LCS with memorization
import sys
sys.setrecursionlimit(10**7)

memo = [[-1] * M for _ in range(N)]

def lcs(i, j):
    if i == N or j == M: #case where i and j reach all items
        return 0

    if memo[i][j] != -1:
        return memo[i][j]

    if A[i] == B[j]:
        memo[i][j] = 1 + lcs(i + 1, j + 1)
    else:
        memo[i][j] = max(lcs(i + 1, j), lcs(i, j + 1))

    return memo[i][j]

print(lcs(0, 0))