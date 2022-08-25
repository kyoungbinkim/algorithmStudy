A,B,C = int(input()),int(input()),int(input())
ans = [0]*10
for s in (str(A*B*C)):
    ans[int(s)]+=1
for i in ans:
    print(i)