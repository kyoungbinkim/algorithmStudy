

def fibo(n):
    if -1 <= n <= 1:
        return n
    
    dir = int(n/abs(n))

    if n < 0 : 
        bef = 1
        now = 0
    else:
        bef = 0
        now = 1
    ans = now + bef
    
    for i in range(2,abs(n)+1,1):
        # tmp = ans
        ans = bef + ans

        bef = now
        now = ans
        print(bef, now, ans)
    if ans == 0:
        print(0)
        print(0)
    elif ans < 0:
        print(-1)
        print(abs(ans))
    else:
        print(1)
        print(ans)

fibo(int(input()))

        
        