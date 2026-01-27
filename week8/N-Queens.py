from collections import deque
import copy

def conflict(Q,i,j):
    #Two queens at columns/rows i and j conflict or same diagonal 
    if Q[i] == Q[j] or abs(Q[i]-Q[j]) == abs(i-j): #
        return True
    else:
        return False

def is_safe(Q, col):
    # Check whether queen at column 'col' conflicts with any earlier queen
    for prev in range(col):
        if conflict(Q, prev, col):
            return False
    return True
   
def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n): #row to place queen
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

class state():
    def __init__(self, n):
        self.Q = [-1]*n
        self.next_col = 0

def successor_states(s, n):
    col = s.next_col
    children = []

    for row in range(n):
        x = copy.deepcopy(s)     # x is successor_state
        x.Q[col] = row

        if is_safe(x.Q, col):
            x.next_col += 1
            children.append(x)

    return children

def Goal(s, n):
    return s.next_col == n


def bfs_n_queens(n):
    
    queue = deque()
    s = state(n)
    queue.append(s)

    while not Goal(s,n):
        for x in successor_states(s,n):
            queue.append(x)
        if not queue:
            return None
        
        s = queue.popleft()

    return s.Q


N = int(input().strip())
sol = bfs_n_queens(N)
if sol is None:
    print("No solution")
else:
    print("Queen list:",sol)
    printqueens(sol)