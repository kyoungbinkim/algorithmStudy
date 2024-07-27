from sys import stdin

t = int(stdin.readline())

for i in range(1, t+1):
    a,b = stdin.readline().split()
    a = int(a)
    b = int(b)
    
    print("Case #{}: {}".format(i, a+b))