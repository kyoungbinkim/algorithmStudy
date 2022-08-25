class heap:
    def __init__(self) -> None:
        self.queue = []
    
    def insert(self, n):
        self.queue.append(n)
        Ind = len(self.queue)-1

        while Ind >= 0:
            parentInd = self.parent(Ind)
            if parentInd >= 0 and self.getVal(parentInd) < self.getVal(Ind):
                self.swapParent(Ind)
                Ind = parentInd
            else:
                break

    def delete(self):
        Ind = len(self.queue)-1
        if Ind <0 :
            return -1
        self.swap(Ind,0)
        maxVal = self.queue.pop()
        self.Heapify(0)
        return maxVal

    
    def Heapify(self, ind): # ind 부터 재정렬
        leftInd = self.leftChild(ind)
        rightInd = self.rightChild(ind)
        maxInd = ind

        for i in [leftInd, rightInd]:
            if self.getVal(maxInd) < self.getVal(i):
                maxInd = i
        
        if maxInd != ind:
            self.swap(maxInd, ind)
            self.Heapify(maxInd)


        

    def swap(self, ind1, ind2):
        self.queue[ind1], self.queue[ind2] = self.queue[ind2], self.queue[ind1]

    def swapParent(self, ind):
        pind = self.parent(ind)
        self.queue[ind], self.queue[pind] = self.queue[pind], self.queue[ind]

    def parent(self, ind):
        ans = (ind-1) // 2
        if ans < 0:
            return -1
        return ans
    
    def leftChild(self, ind):
        ans = ind*2 +1
        if ans >= len(self.queue):
            return -1
        return ans

    def rightChild(self, ind):
        ans = ind*2 + 2
        if ans >= len(self.queue):
            return -1
        return ans
    
    def getVal(self, ind):
        if ind >= len(self.queue) or ind < 0:
            return -1
        return self.queue[ind]

if __name__ =="__main__":
    myHeap = heap()
    for i in range(2,12,2):
        myHeap.insert(i)
    for i in ([13,7,9]):
        myHeap.insert(i)
    
    print(myHeap.queue)

    for _ in range(4):
        print(myHeap.delete())