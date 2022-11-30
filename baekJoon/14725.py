from sys import stdin


class antNode:
    def __init__(self, val):
        self.val = val
        self.child = []
    
    def getVal(self):
        return self.val        

    def getNode(self, v):
        for node in self.child:
            if node.getVal() == v:
                return node
        return None
    
    # true 면 없음
    def check(self, n):
        for s in self.child:
            if s.getVal() == n:
                return False
        return True

    def append(self, n):
        self.child.append(antNode(n))
        

def printNode(cnt, node):
    if node.child == []:
        return
    node.child.sort(key=lambda x: x.getVal())
    # print(cnt, node.val, [x.getVal() for x in node.child])
    for n in node.child:
        print("{}{}".format("--"*cnt,n.val))
        printNode(cnt+1,n)

n = int(stdin.readline())
rt = antNode(0)
for _ in range(n):
    tmp = list(stdin.readline().split())
    size= int(tmp[0])
    tmp = tmp[1:]

    if rt.check(tmp[0]):
        node= rt
        for i in range(size):
            node.append(tmp[i])
            node = node.getNode(tmp[i])
        continue

    node = rt

    for t in tmp:
        if node.getNode(t) == None:
            node.append(t)
        node = node.getNode(t)


    
    
printNode(0, rt)
    
    
    

    


