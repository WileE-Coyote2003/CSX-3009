from simplePriorityQueue import Simple_Priority_Queue
from sys import stdin
INF = 1000000000
V = int(input())
adj = [[] for i in range(V)]

for line in stdin:
    x = line.split()
    u = int(x[0])
    v = int(x[1])
    w = int(x[2])
    adj[u].append((v,w))
    adj[v].append((u,w))