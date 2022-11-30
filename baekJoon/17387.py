from sys import stdin

class poly:
    def __init__(self, x1,y1, x2,y2):
        self.x1, self.x2 = x1, x2
        self.y1, self.y2 = y1, y2
        self.left, self.right = min(x1,x2), max(x1,x2)
        self.up, self.down = max(y1,y2), min(y1,y2)
        if x1==x2:
            self.gradient = float("inf")
        else:
            self.gradient = (y2-y1) / (x2-x1)
            self.yintercept = y1 - self.gradient * x1
    
    def Print(self):
        print(self.gradient, self.yintercept)

    def eval(self, n):
        if self.gradient == float("inf"):
            return self.x1
        return self.yintercept + self.gradient * n

    def inter(self, p):
        l,r = max(self.left, p.left), min(self.right, p.right)
        if self.gradient == float("inf") and  p.gradient == float("inf"):
            if self.x1 == p.x1 and min(p.up, self.up) >= max(p.down, self.down):
                return 1
            return 0
        elif self.gradient == float("inf"):
            if self.down <= p.eval(self.x1) <= self.up+ 0.00000001 and p.left- 0.00000001 <= self.x1 <= p.right+ 0.00000001:
                return 1
            return 0
        elif p.gradient == float("inf"):
            if p.down <= self.eval(p.x1) <= p.up+ 0.00000001 and self.left- 0.00000001 <= p.x1 <= self.right+ 0.00000001:
                return 1
            return 0
        if self.gradient == p.gradient:
            if self.yintercept == p.yintercept:
                if l > r:
                    return 0
                return 1
            else:
                return 0
        
        x = (self.yintercept - p.yintercept) / (p.gradient - self.gradient)

        if l - 0.00000001<= x <= r + 0.00000001:
            return 1
        return 0


a,b,c,d = map(int, stdin.readline().split())
poly1 = poly(a,b,c,d )
a,b,c,d = map(int, stdin.readline().split())
poly2 = poly(a,b,c,d )
print(poly1.inter(poly2))