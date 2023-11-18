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
            if self.x1 == p.x1 and min(p.up, self.up) == max(p.down, self.down):
                return [p.x1, min(p.up, self.up)]
            elif self.x1 == p.x1 and min(p.up, self.up) > max(p.down, self.down):
                return 2
            return 0
        elif self.gradient == float("inf"):
            if self.down- 10**-7 <= p.eval(self.x1) <= self.up+ 10**-7 and p.left <= self.x1 <= p.right:
                return [self.x1, p.eval(self.x1)]
            return 0
        elif p.gradient == float("inf"):
            if p.down- 10**-7 <= self.eval(p.x1) <= p.up+ 10**-7 and self.left <= p.x1 <= self.right:
                return [p.x1, self.eval(p.x1)]
            return 0
        if self.gradient == p.gradient:
            if self.yintercept == p.yintercept:
                if l > r:
                    return 0
                elif l==r:
                    return [l, self.eval(l)]
                return 2
            else:
                return 0
        
        x = (self.yintercept - p.yintercept) / (p.gradient - self.gradient)

        if l - 10**-7<= x <= r + 10**-7:
            return [x, self.eval(x)]
        return 0


x1,y1,x2,y2 = map(int ,stdin.readline().split())
line1 = poly(x1,y1,x2,y2)
x1,y1,x2,y2 = map(int ,stdin.readline().split())
line2 = poly(x1,y1,x2,y2)

inter = line1.inter(line2)
if inter == 0 or inter == 2:
    print((inter>0)*1)
else:
    print(1)
    print("{} {}".format(inter[0], inter[1]))