dir = [(0,0), (-1, 0 ), (0, 1), (1,0), (0,-1)]

class WirelessCharge:
    def __init__(self, t):
        self.ans = 0
        self.m, self.a = map(int, input().split())

        self.dirA = list(map(int, input().split()))
        self.dirB = list(map(int, input().split()))

        self.chargers = []
        for _ in range(self.a):
            r,c, dist, power = map(int, input().split())

            self.chargers.append((c-1, r-1, dist, power))

        self.posA, self.posB = (0, 0), (9, 9)
        self.calcPower()

        for i in range(self.m):
            self.posA = (self.posA[0] + dir[self.dirA[i]][0], self.posA[1] + dir[self.dirA[i]][1])
            self.posB = (self.posB[0] + dir[self.dirB[i]][0], self.posB[1] + dir[self.dirB[i]][1])
            self.calcPower()
            
        print('#{} {}'.format(t, self.ans))

    def calcPower(self):
        candiA, candiB = [(0,0,0,0)], [(0,0,0,0)]

        for charger in self.chargers:
            if abs(self.posA[0] - charger[0]) + abs(self.posA[1] - charger[1]) <= charger[2]:
                candiA.append(charger)

            if abs(self.posB[0] - charger[0]) + abs(self.posB[1] - charger[1]) <= charger[2]:
                candiB.append(charger)

        maxAns = 0
        for c1 in candiA:
            for c2 in candiB:

                if c1 == c2:
                    continue

                if c1[3] + c2[3] > maxAns:
                    maxAns = c1[3] + c2[3]
        self.ans += maxAns




T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    WirelessCharge(test_case)
