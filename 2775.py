
for _ in range(int(input())):
    
    a,b = int(input()), int(input())
    ans = list(range(1,b+1))

    for _ in range(1, a+1):

        tmp = ans.copy()
        for i in range(b):
            ans[i] = sum(tmp[:i+1])
    print(ans[b-1])

