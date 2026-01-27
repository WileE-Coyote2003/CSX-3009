def printqueens(Q):
    n = len(Q)
    board = [['.']*n for i in range(n)]
    for j in range(n): #row to place queen
        board[Q[j]][j] = 'Q'
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='')
        print()

Q = [1, 3, 0, 2]
printqueens(Q)            

