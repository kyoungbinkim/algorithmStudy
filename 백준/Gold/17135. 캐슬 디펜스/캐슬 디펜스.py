from sys import stdin
from collections import deque

dir = [
    (0,-1),
    (-1,0),
    (0, 1),
]


class CastleDeffense:
    def __init__(self):
        self.n, self.m, self.d = map(int, stdin.readline().split())
        self.board = [list(map(int, stdin.readline().split())) for _ in range(self.n)]
        

    def clear(self):
        self.sim = [a.copy() for a in self.board]
        self.offset = self.n-1

    def makeArchers(self, aList, idx=0):
        tmp = []    

        if idx == self.m:
            for a in aList:
                if len(a) == 3:
                    tmp.append(a)
            return tmp
        
        for a in aList:
            tmp.append(a)
            if len(a) < 3:
                tmp.append(a + [idx])

        return self.makeArchers(tmp, idx + 1)
    
    def deffense(self, archer):
        ans = set()
        for col in archer:
            x, y = self.offset, col
            que = deque([(x,y,1)])
            while len(que):
                r, c, dist = que.popleft()

                if 0<= r < self.n and 0 <= c < self.m:
                    if self.sim[r][c] == 1:
                        ans.add((r,c))
                        break
                    elif dist < self.d:
                        for d in dir:
                            que.append((r+d[0], c+d[1], dist+1))

        self.offset -= 1
        for r, c in ans:
            self.sim[r][c] = 0
        return len(ans)
        

    def calcMaxKill(self):
        archers = self.makeArchers([[]], 0)

        kill = 0
        for archer in archers:
            self.clear()
            tmp = 0
            for _ in range(self.n):
                tmp += self.deffense(archer)
            kill = max(kill, tmp)
        print(kill)

cd = CastleDeffense()
cd.calcMaxKill()