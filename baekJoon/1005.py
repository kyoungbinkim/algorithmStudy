
class timeService: 
    def __init__(self, tSize, tArr):
        self.ans = 0
        self.maplen = tSize
        self.map = [] # 나를 가르키는 node ind
        for _ in range(tSize):
            self.map.append([False] * tSize)
        self.timeArr = tArr
    
    def update(self, rule):
        self.map[rule[1]-1][rule[0]-1] = True
        
    
    def run(self, target):
        visit = {}
        while True:
            t = 0
            tind = []
            for i in range(self.maplen):
                # print(sum(self.map[i]))
                if sum(self.map[i]) == 0 and visit.get(i) == None:
                    visit.update({i:True})
                    tind.append(i)
                    if t < self.timeArr[i]:
                        t = self.timeArr[i]
            self.ans += t
            for ind in tind:
                if ind == target-1:
                    return
                for m in self.map:
                    m[ind] = False
        

def string2intArr(strings):
    tmp = []
    for s in strings.split():
        tmp.append(int(s))
    return tmp

for _ in range(int(input())):
    timeSize, ruleSize = string2intArr(input())
    timeArr = string2intArr(input())
    tService = timeService(timeSize, timeArr)
    for _ in range(ruleSize):
        tService.update(string2intArr(input()))
    tService.run(int(input()))
    print(tService.ans)