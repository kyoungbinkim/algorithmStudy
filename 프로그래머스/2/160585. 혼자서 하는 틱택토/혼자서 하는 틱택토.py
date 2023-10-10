from copy import deepcopy

ansList = set()

char2num = {
    'O' : 1,
    '.' : 0,
    'X' : -1
}

def isEnd(board):
    leftDown, rightDown = board[0][0] != 0, board[2][0] != 0
    
    for i in range(3):
        row, col = board[i][0] != 0, board[0][i] != 0
        
        for j in range(1,3):
            row = row and board[i][0] == board[i][j] 
            col = col and board[0][i] == board[j][i]
        if row or col:
            return True
        leftDown = leftDown and board[0][0] == board[i][i]  
        rightDown = rightDown and board[2][0] == board[2-i][i]
    
    
    return leftDown or rightDown
    
def boardToTuple(board):
    ans = ()
    for b in board:
        ans += tuple(b)
    return ans
    
def DFS(board, turn):
    if boardToTuple(board) in ansList:
        return
    
    ansList.add(boardToTuple(board))
    
    if isEnd(board):
        return
        
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                newBoard = deepcopy(board)
                newBoard[i][j] = turn
                DFS(newBoard, -1 * turn)

def solution(board):
    
    DFS([[0 for _ in range(3)] for _ in range(3)], 1)
    
    t, inv = (), ()
    
    for b in board:
        for c in b:
            t += tuple([char2num[c]])
            inv += tuple([-1 * char2num[c]])
    print(t, inv)
    # print(t in ansList, inv in ansList)
    
    
    answer = 1 if (t in ansList) else 0
    return answer