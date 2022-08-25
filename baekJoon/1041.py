# ACFD ABFE  -> AC CF FD DA  AB BF FE EA / AB AC AD AE BC BD BF CE CF DE DF EF
# AEC AED ABC ABD BFC BFD EFC EFD

n = int(input())
dice = list(map(int, input().split()))

def calcMin2(dice):
    ans = 100
    for i in range(len(dice)):
        for j in range(len(dice)):
            if i==j or i+j == 5:
                continue
            if ans > dice[i]+dice[j]:
                ans = dice[i]+dice[j]
    return ans

def calcMin3(dice):
    ans = 150
    for i in range(len(dice)):
        for j in range(len(dice)):
            if i==j or i+j == 5:
                continue
            for k in range(len(dice)):
                if i==k or j==k or i+k==5 or j+k==5:
                    continue
                if ans > dice[i]+dice[j]+dice[k]:
                    ans = dice[i]+dice[j]+dice[k]
    return ans
                
if n == 1:
    print(sum(dice)-max(dice))
else:
    min2 = calcMin2(dice)
    min3 = calcMin3(dice)
    # print(min2, min3)
    # 1개  4 * (n-2)* (n-1) + (n-2)*(n-2)
    # 2개  4*(n-1) + 4* (n-2)
    # 3개  4
    ret = min(dice) * (4*(n-2)*(n-1) + (n-2)*(n-2)) 
    ret += min2 * (4*(2*n -3))
    ret += min3 * 4
    print(ret)