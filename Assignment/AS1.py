# ULTIMATE GREYNESS
# Name: Thwin Htoo Aung
# ID: 6612109

import sys

data = sys.stdin.read().strip().split()
idx = 0

n = int(data[idx])
idx += 1

colors = []
for _ in range(n):
    v = int(data[idx])
    d = int(data[idx + 1])
    idx += 2
    colors.append((v, d))

best = None

# Enumerate all non-empty subsets
for mask in range(1, 1 << n):
    vivid_product = 1
    dull_sum = 0

    for i in range(n):
        if mask & (1 << i):
            vivid_product *= colors[i][0]
            dull_sum += colors[i][1]

    diff = abs(vivid_product - dull_sum)

    if best is None or diff < best:
        best = diff

print(best)