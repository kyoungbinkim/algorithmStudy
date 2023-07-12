from sys import stdin

x,b = map(int, stdin.readline().split())

# print(x//b , x%b)

def convertN(x,b):
    q, r = divmod(x, b)
    # print(q,r)

    if r<0:
        r += abs(b)
        q -= b // abs(b)
    # print(q,r)

    return q,r

def convert(x,b):
    ans = 0
    ten = 1
    while abs(x)>1:

        x,r = convertN(x,b)
        ans += r * ten
        ten *= 10

    if x<0:
        x,r = convertN(x,b)
        ans += r * ten
        ten *= 10
    ans += x * ten
    return ans

if x<0 and b>0:
    x = abs(x)
    print(convert(x,b) * -1)
else:
    print(convert(x,b))

