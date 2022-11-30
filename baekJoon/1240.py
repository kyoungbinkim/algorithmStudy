from sys import stdin

class node:
    def __init__(self, ind):
        self.ind = ind
        self.link = {"p":None, "c":[]}
    
    def setP(self, pind, plen):
        self.link["p"] = [pind, plen]
    
    def setC(self, cind, clen):
        self.link["c"].append([cind, clen])
    
    def getP(self):
        return self.link["p"]
    
    def getC(self):
        return self.link["c"]
    
    def printNode(self):
        print("ind : ",self.ind)
        print("parent : ", self.link["p"])
        print("child : ", self.link["c"])
        print()    


class Tree:
    def __init__(self, size):
        self.size = size
        self.nodeList = [0]
        for i in range(1,size+1):
            self.nodeList.append(node(i))
    
    def update(self, info):
        p,c,l = info

        if self.nodeList[c].getP() == None:
            self.nodeList[p].setC(c,l)
            self.nodeList[c].setP(p,l)
        else:
            self.nodeList[p].setP(c,l)
            self.nodeList[c].setC(p,l)
    
    def printTree(self):
        for n in self.nodeList:
            if n==0:
                continue
            n.printNode()
    
    def getAllc(self, ind):
        ans = []
    
    def getAllp(self, ind):
        i = [ind,0]
        ans = [i]
        while self.nodeList[i[0]].getP() != None:
            tmp = ans[len(ans)-1].copy()
            i = self.nodeList[i[0]].getP()
            ans.append([i[0], i[1]+tmp[1]])
        return ans

    
    def search(self, start, end):
    
        sP = self.getAllp(start)
        eP = self.getAllp(end)
        print(sP, eP)

        for i in range(len(sP)):
            for j in range(len(eP)):
                if sP[i][0] == eP[j][0]:
                    return sP[i][1] + eP[j][1]
    
            
n, ansNum = map(int, stdin.readline().split())

myTree = Tree(n)
for _ in range(n-1):
    myTree.update(list(map(int, stdin.readline().split())))
myTree.printTree()

for _ in range(ansNum):
    start, end = map(int, stdin.readline().split())
    print(myTree.search(start, end))

# 5 3
# 2 1 2
# 4 3 2
# 1 4 3
# 5 3 5
# 1 2
# 4 2
# 5 1

# 7 3
# 1 4 5
# 5 1 3
# 1 2 3
# 2 3 8
# 7 4 3
# 5 6 12
# 1 6
# 5 3
# 7 3