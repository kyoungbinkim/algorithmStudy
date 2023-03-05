## BAD solution 2^n ##

from sys import stdin

num, maxW = map(int ,stdin.readline().split())

class stuff:

    def __init__(self, w, v, bound=maxW) -> None:
        self.bound = bound
        self.w = w
        self.v = v

    def update(self, s):
        if self.w + s.w <= self.bound:
            self.w += s.w
            self.v += s.v
            return True
        else:
            return False
    
    def showVal(self):
        print(self.v)

def add(s1, s2):
    if s1.w+s2.w > maxW:
        return None
    return stuff(s1.w+s2.w, s1.v+s2.v)

def cmp(s1, s2):
    return s1 if s1.v > s2.v else s2

stuffL = []
for i in range(num):
    w,v = map(int, stdin.readline().split())        
    stuffL.append(stuff(w,v))

def calc(stuffList, idx, package:stuff):
    if idx+1 == num:
        package.update(stuffList[idx])
        return package

    package_add = add(package, stuffList[idx])

    if package_add == None:
        return calc(stuffList, idx+1, package)
    return cmp(
        calc(stuffList, idx+1, package),
        calc(stuffList, idx+1, package_add)
    )
        
ret = calc(stuffL, 0, stuff(0, 0))
ret.showVal()
