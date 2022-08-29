class fiboMat:
    def __init__(self):
        self.square = [[1,1], [1,0]]
        self.ans = [[1,0],[0,1]]
        self.p = 1000000007
    
    def __matMul__(self, m1, m2):
        tmp = [[0,0],[0,0]]
        tmp[0][0] = (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % 1000000007
        tmp[0][1] = (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % 1000000007
        tmp[1][0] = (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % 1000000007
        tmp[1][1] = (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % 1000000007
        return tmp

    def __matSquare__(self):
        self.square = self.__matMul__(self.square, self.square)
    
    def pow(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        nbin = bin(n-1)[2:]

        for s in nbin[::-1]:
            
            if s=='1':
                self.ans = self.__matMul__(self.ans, self.square)
            self.__matSquare__()
        return self.ans[0][0]
        
 
n = int(input())
f = fiboMat()
print(f.pow(n))
