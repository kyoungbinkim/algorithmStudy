hexdic = {}
for i in range(16):
    hexdic.update({i: hex(i)[2:].upper()})
# print(hexdic)

class baseN:
    def __init__(self, n, dec):
        self.n = n
        self.dec = dec
        self.baseN = None
        self.ans = ''
        self.dec2baseN()
        
    def dec2baseN(self):
        tmp = ''
        copyn = self.dec
        while copyn >= self.n:
            tmp += hexdic[copyn % self.n]
            copyn = copyn // self.n
        tmp += hexdic[copyn]
        # print("tmp" , tmp[::-1])
        self.baseN = tmp[::-1]
    
    def plus(self):
        self.dec +=1
        self.dec2baseN()
        
    def run(self, t, m,p):
        ind = 0
        print("baseN : ", self.baseN)
        while len(self.ans) < t:
            for i in range(len(self.baseN)):
                if ind % m == p-1:
                    self.ans += self.baseN[i]
                if len(self.ans) >= t:
                    break
                ind += 1
            # print("ans : ",self.ans)
            self.plus()
    
        
        
def solution(n, t, m, p):
    b = baseN(n,0)
    b.run(t,m,p)
    answer = ''
    return b.ans