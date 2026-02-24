import sys
sys.setrecursionlimit(1000000)

def can_pass(start, H, T, grid):
    visited = [[False] * (H + 1) for _ in range(T)]

    def dfs(t, h):
        # out of bounds
        if h < 1 or h > H:
            return False
        
        # obstacle
        if grid[t][h - 1] == 1:
            return False
        
        # reached last interval
        if t == T - 1:
            return True
        
        if visited[t][h]:
            return False
        
        visited[t][h] = True

        # try all 3 moves
        return (
            dfs(t + 1, h) or
            dfs(t + 1, h + 1) or
            dfs(t + 1, h - 1)
        )

    return dfs(0, start)


# MAIN
H, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(T)]

for start in range(1, H + 1):
    if can_pass(start, H, T, grid):
        print(start)
        break