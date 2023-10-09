from sys import stdin

class Monomino:
    def __init__(self):
        self.score = 0
        self.red  =[ [0 for _ in range(4)] for _ in range(6) ]
        self.blue =[ [0 for _ in range(4)] for _ in range(6) ]

        n = int(stdin.readline())
        for _ in range(n):
            t,x,y = map(int, stdin.readline().split())
            block = [(x,y)]
            if t == 2:
                block.append((block[0][0], block[0][1] + 1))
            elif t == 3:
                block.append((block[0][0] + 1, block[0][1]))

            self.moveBlock(self.blue, self.parseBlock(block)[0])
            self.moveBlock(self.red, self.parseBlock(block)[1])

            while self.removeLine(self.red):
                pass
            
            while self.removeLine(self.blue):
                pass
            
            self.goDown(self.red)
            self.goDown(self.blue)

        print(self.score)
        print(sum([sum(b) for b in self.red]) + sum([sum(b) for b in self.blue]))



    def parseBlock(self, block):
        b,r = [(0,block[0][0])], [(0, block[0][1])]

        if len(block) > 1:
            x,y = block[1]
            b.append((int(x == b[0][1]), x))
            r.append((int(y == r[0][1]), y))

        return (b, r)
    
    def moveBlock(self, board, blocks):
        now = blocks
        next = [ (x+1, y) for (x,y) in blocks]
        
        while sum([board[x][y] for (x,y) in next]) == 0:
            now = next
            next = [ (x+1, y) for (x,y) in now]
            
            FLAG = False
            for (r,c) in next:
                if r > 5:
                    FLAG = True
            if FLAG:
                break
        
        for (r,c) in now:
            board[r][c] = 1

    
    def removeLine(self, board):
        
        for (line, idx) in zip(board, range(6)):
            if sum(line) == 4:
                board.pop(idx)
                self.score += 1
                board.insert(0, [0,0,0,0])

                return True
        
        return False
    
    def goDown(self, board):
        cnt = 0

        for i in range(2):
            if sum(board[i]) > 0 :
                cnt +=1
        
        for i in range(cnt):
            board.pop()
            board.insert(0,[0,0,0,0])

Monomino()
