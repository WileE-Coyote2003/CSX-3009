import sys

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    ra = find(parent, a)
    rb = find(parent, b)

    if ra == rb:
        return False

    if rank[ra] < rank[rb]:
        parent[ra] = rb
    elif rank[ra] > rank[rb]:
        parent[rb] = ra
    else:
        parent[rb] = ra
        rank[ra] += 1

    return True

# ---- INPUT ----
data = sys.stdin.read().strip().split()
idx = 0

V = int(data[idx]); idx += 1
E = int(data[idx]); idx += 1

edges = []
for _ in range(E):
    u = int(data[idx]); v = int(data[idx+1]); w = int(data[idx+2])
    idx += 3
    edges.append((w, u, v))

# ---- KRUSKAL ----
edges.sort()

parent = list(range(V))
rank = [0] * V

mst_cost = 0
edge_count = 0

for w, u, v in edges:
    if union(parent, rank, u, v):
        mst_cost += w
        edge_count += 1
        if edge_count == V - 1:
            break

# ---- OUTPUT ----
print(mst_cost)