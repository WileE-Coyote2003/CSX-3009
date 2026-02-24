from collections import deque

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

visited = [[False] * N for _ in range(M)]

def bfs(sr, sc):
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    size = 0

    while q:
        r, c = q.popleft()
        size += 1

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < M and 0 <= nc < N:
                if not visited[nr][nc] and grid[nr][nc] == 1:
                    visited[nr][nc] = True
                    q.append((nr, nc))
    return size

max_cloud = 0

for r in range(M):
    for c in range(N):
        if grid[r][c] == 1 and not visited[r][c]:
            max_cloud = max(max_cloud, bfs(r, c))

print(max_cloud)