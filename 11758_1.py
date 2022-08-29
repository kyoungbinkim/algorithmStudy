x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

v1 = [x2-x1, y2-y1]

b = (x1-x2)
a = (y2-y1)
c = -1 * (a * x1 + b * y1)

if b<0:
    a = -1 * a
    b = -1 * b
    c = -1 * c
# print(a,b,c, v1, a*x3 + b*y3 + c)
if a*x3 + b*y3 + c == 0:
    print(0)
else:
    if b==0:
        if v1[1] >0:  
            if x3 > x1:
                print(-1)
            else:
                print(1)
        else:
            if x3 > x1:
                print(1)
            else:
                print(-1)
    elif a == 0:
        if v1[0] >0:  
            if y3 > y1:
                print(1)
            else:
                print(-1)
        else:
            if y3 > y1:
                print(-1)
            else:
                print(1)
    elif v1[0] > 0:
        if a*x3 + b*y3 + c < 0:
            print(-1)
        else:
            print(1)
    else:
        if a*x3 + b*y3 + c < 0:
            print(1)
        else:
            print(-1)