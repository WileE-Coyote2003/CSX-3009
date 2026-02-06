
n = int(input().strip())
#I store start time and finish time of activity
s = []
f = []

for _ in range(n):
    start, finish = map(int, input().split())
    s.append(start)
    f.append(finish)

order = sorted(range(n), key=lambda i: f[i]) #then sort activites based on finished time 

s = [s[i] for i in order]
f = [f[i] for i in order]

count = 1 # start from first activity 

last_finished = f[0]

for i in range(1,n):
    if s[i] >= last_finished: # check for overlap
        count +=1 #if is not overlap update the no of activity
        last_finished = f[i] #store last finish time of the activity

print(count)