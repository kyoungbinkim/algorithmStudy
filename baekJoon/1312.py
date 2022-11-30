

def factorization(x):
    d = 2
    ans = {}
    while d <= x:
        if x % d == 0:
            if ans.get(d) == None:
                ans.update({d:1})
            else:
                ans[d] += 1
            x = x / d
        else:
            d = d + 1
    return ans


for _ in range(int(input())):
    n = int(input())
    ans = factorization(n)
    keyl = list(ans.keys())
    keyl.sort()

    for k in keyl:
        print(k, ans[k])
    