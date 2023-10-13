from collections import deque
from copy import deepcopy

dir = [
    (1,0), (-1,0), (0,1), (0,-1)
]

class Game:
    def __init__(self, t):
        self.k, self.m, self.n = map(int, input().split())

        self.board = [list(map(int, input().split())) for _ in range(self.n)][::-1]
		
        ans = self.Run(self.board, 0)
        print('#{} {}'.format(t, ans))

    def Run(self, b, cnt):

        if cnt >= self.k or sum([sum([int(x>0) for x in b[i]]) for i in range(self.n)]) == 0:

            return sum([sum([int(x>0) for x in b[i]]) for i in range(self.n)])

        ans = float('inf')
        for i in range(self.m):

            for j in range(self.n-1, -1, -1):
                if b[j][i] > 0:
                    points = self.getPoint((j,i), b)

                    ans = min(ans, self.Run(self.remove(b, points), cnt+1))
                    break
        return ans

    def getPoint(self, pos, b):
        visit = set([pos])
        que = deque([pos])

        while len(que):
            p = que.popleft()
            v = b[p[0]][p[1]]

            for d in dir:
                for dist in range(1, v):
                    dr, dc = p[0] + dist * d[0], p[1] + dist * d[1]

                    if dr < 0 or dc < 0 or dr >= self.n or dc >= self.m or (dr,dc) in visit or b[dr][dc] == 0:
                        continue

                    visit.add((dr,dc))
                    que.append((dr,dc))
        return visit

    def remove(self, b, visit):

        after = deepcopy(b)
        for (r,c) in visit:

            for d in dir:
                for i in range(b[r][c]):
                    dr, dc = r + i*d[0] ,c + i*d[1]

                    if dr < 0 or dc < 0 or dr >= self.n or dc >= self.m:
                        break

                    after[dr][dc] = 0

        return self.gravity(after)

    def gravity(self, b):

        for i in range(self.n):
            for j in range(self.m):
                if b[i][j]:
                    now = (i,j)

                    while 1:
                        dr,dc = now[0]-1, now[1]

                        if dr <0 or b[dr][dc]:
                            break

                        now = (dr,dc)

                    b[i][j], b[now[0]][now[1]] = 0, b[i][j]
        return b


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    Game(test_case)