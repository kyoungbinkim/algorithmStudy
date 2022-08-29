# ax + by +c =0
# y = -1/b (ax + c)


x1,y1 = map(int, input().split())
x2,y2 = map(int, input().split())
x3,y3 = map(int, input().split())

if x1==x2:
    a1=y2-y1
    b1=0
    c1= -1 * x1 * a1
else:
    b1 = (x1-x2)
    a1 = (y2-y1)
    c1 = -1 * (a1 * x1 + b1 * y1)

if a1 * x3 + b1 * y3 + c1 == 0:
    print(0)
elif b1 == 0:
    if a1 > 0:
        if x1 < x3:
            print(-1)
        else:
            print(1)
    else:
        if x1 <x3:
            print(1)
        else:
            print(-1)
elif a1 == 0:
    if b1 < 0: # 오른방향
        if y1 <y3:
            print(-1)
        else:
            print(1)
    else:
        if y1 <y3:
            print(1)
        else:
            print(-1)

elif a1 * b1 < 0:
    if y3 < -1 * (a1 * x3 + c1) / b1:
        print(-1)
    else:
        print(1)
else:
    if y3 < -1 * (a1 * x3 + c1) / b1:
        print(1)
    else:
        print(-1)



