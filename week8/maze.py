from collections import deque
import sys

input = sys.stdin.readline

M, N = map(int, input().split())
sr, sc = map(int, input().split())
tr, tc = map(int, input().split())

maze = [list(map(int, input().split())) for _ in range(M)]

# If start or destination is a wall, no path
if maze[sr][sc] == 1 or maze[tr][tc] == 1:
    print(-1)
    sys.exit()

dist = [[-1] * N for _ in range(M)]
q = deque([(sr, sc)])
dist[sr][sc] = 0  # number of moves from start

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while q:
    r, c = q.popleft()
    if (r, c) == (tr, tc):
        break

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < M and 0 <= nc < N and maze[nr][nc] == 0 and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

d = dist[tr][tc]
if d == -1:
    print(-1)
else:
    print(d + 1)  # number of tiles on the route (tiles = moves + 1)