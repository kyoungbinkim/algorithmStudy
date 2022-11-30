from sys import stdin

# a/m - b/n = a-b / m-n

# an - mb /  nm = a-b / m-n

# (an-mb)(m-n) - (a-b)nm = 0

# anm -m^2 b -an^2 +nmb - anm +bnm= 0

# -m^2 b - n^2 a + 2bnm = 0

# m^2/n^2 = - a/b

while True:
    b,n = map(int, stdin.readline().split())
    if b == n == 0:
        break
    
    
    
