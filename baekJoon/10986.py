from sys import stdin

size, num = map(int, stdin.readline().split())
numArr = list(map(int, stdin.readline().split()))

ansArr = [0 for _ in range(num)] 
ans = [0]
for i in range(size):
    ans.append(ans[i]+ numArr[i])
    ansArr[ans[i+1] % num] += 1

cnt = ansArr[0]
for n in ansArr:
    if n <= 1:
        continue
    cnt += n * (n-1) //2
print(cnt)
    

