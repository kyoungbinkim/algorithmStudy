import sys
sys.setrecursionlimit(10**9)

class node:
    def __init__(self, ind, p=None, c=None):
        self.ind = ind
        self.p = p
        self.c = c
    
    def nodePrint(self):
        print("ind : ", self.ind)
        print("p : ", self.p)
        print("c : ", self.c)



class Graph:
    def __init__(self, size):
        self.size = size
        self.arr = []
        for i in range(1, size+1):
            self.arr.append(node(i, c=(nSum(i)+i)%size))
            if self.arr[i-1].c == 0:
                self.arr[i-1].c = size

        for i in range(size):
            self.arr[self.arr[i].c-1].p = i+1

    def DFS(self, visit, n):
        visit.add(n)
        if self.arr[n-1].c in visit:
            return 1

        return self.DFS(visit, self.arr[n-1].c) + 1

    
    def run(self):
        ans = -1
        for i in range(self.size):
            if self.arr[i].p == None:
                tmp = self.DFS(set([]), i+1)
                if tmp > ans:
                    ans = tmp
        
        if ans == -1:
            ans = self.DFS(set([]),1)
        print(ans)
    


def nSum(n):
    ans = 0
    tmp = n
    while tmp >0:
        ans += tmp%10
        tmp = tmp//10
    return ans


def DFS(mod, visit, n, ans):
    visit.add(n)
    tmp = nSum(n)
    next = (tmp+n)%mod
    if next == 0:
        next = mod
    if next in visit:
        return 1

    return DFS(mod, visit, next)+1

k = int(input())
myG = Graph(k)
myG.run()