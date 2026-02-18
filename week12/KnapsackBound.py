class obj:
    def __init__(self, w, v):
        self.w = w
        self.v = v
        self.r = v / w


x = input().split()
N = int(x[0])
M = int(x[1])

w = input().split()
v = input().split()

item = []
for i in range(N):
    item.append(obj(int(w[i]), int(v[i])))

# Required for correct bounding
def getKey(x):
    return x.r

item.sort(key=getKey, reverse=True)


def Bound(i, C):
    global item, N
    
    sw = 0
    sv = 0
    j = i
    f = 1.0
    
    while j < N and f == 1.0:
        wj = min(C - sw, item[j].w)
        f = float(wj) / item[j].w
        sw += f * item[j].w
        sv += f * item[j].v
        j += 1
    
    return sv


maxV = 0
count = 0

def dfs(i, sumW, sumV):
    global maxV, count, N, M, item
    
    count += 1
    
    # Prune overweight
    if sumW > M:
        return
    
    # Bounding prune
    if sumV + Bound(i, M - sumW) <= maxV:
        return
    
    if i == N:
        maxV = max(maxV, sumV)
    else:
        # Compute bound for both branches
        skipBound = sumV + Bound(i+1, M - sumW)
        takeBound = -1
        
        if sumW + item[i].w <= M:
            takeBound = sumV + item[i].v + Bound(i+1, M - (sumW + item[i].w))
        
        # Explore more promising branch first
        if takeBound > skipBound:
            dfs(i+1, sumW + item[i].w, sumV + item[i].v)
            dfs(i+1, sumW, sumV)
        else:
            dfs(i+1, sumW, sumV)
            dfs(i+1, sumW + item[i].w, sumV + item[i].v)

dfs(0, 0, 0)

print(maxV)
print(count)