from sys import stdin
from copy import deepcopy

class Sudoku:
    def __init__(self) -> None:
        self.board, self.ans = [], None
        
        cnt, self.zeros = [0 for _ in range(10)], []
        for i in range(9):
            tmp = []
            for (j,c) in enumerate(stdin.readline().removesuffix('\n')):
                tmp.append(int(c))
                if int(c) > 0:
                    cnt[int(c)] += 1
                else:
                    self.zeros.append((i,j))
            self.board.append(tmp)
        self.visit= [set(l) for l in self.board]
        r,c = self.zeros[0]
        self.dfs(self.board, cnt, 0)
        for l in self.ans:
            print("".join([str(c) for c in l]))

    
    def isValid(self,b):

        for i in range(9):
            if sum(b[i]) != 45:
                return False

            if sum([b[j][i] for j in range(9)]) != 45:
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                ans = 0
                for k in range(3):
                    ans += sum(b[i+k][j : j+3])
                if ans != 45:
                    return False
        return True

    def dfs(self, b, cnt, zeroIdx):

        if zeroIdx == len(self.zeros):
            self.ans = b
            return
        
        r,c = self.zeros[zeroIdx]
        row = set(b[r])
        col = set([b[j][c] for j in range(9)])
        tmp = []
        
        RR = (r//3) * 3
        CC = (c//3) * 3

        for i in range(RR, RR+3):
            tmp += b[i][CC:CC+3]
        box = set(tmp)

        newBoard = [l.copy() for l in b]
        for i in range(1, 10):
            
            if cnt[i] == 9 or i in row or i in col or i in box:
                continue
            
            newBoard[r][c] = i
            newCnt = cnt.copy()
            newCnt[i] += 1

            self.dfs(newBoard, newCnt, zeroIdx+1)
            if self.ans != None:
                return

Sudoku()