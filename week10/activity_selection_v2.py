n = int(input().strip())
#I store start time and finish time of activity
s = []
f = []

for _ in range(n):
    start, finish = map(int, input().split())
    s.append(start)
    f.append(finish)

# v2: sort activities based on START time
order = sorted(range(n), key=lambda i: s[i])

s = [s[i] for i in order]
f = [f[i] for i in order]

count = 1  # start from first activity
last_finished = f[0]

for i in range(1, n):
    if s[i] >= last_finished:  # check for overlap
        count += 1
        last_finished = f[i]

print(count)