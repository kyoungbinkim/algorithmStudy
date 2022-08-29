from sys import stdin

n, strLen = int(stdin.readline()), int(stdin.readline())
string = stdin.readline().replace('\n','')
Pn = "IO"*n + "I"

ans = 0
for i in range(strLen-2*n):
    if string[i:i+2*n+1] == Pn:
        ans += 1
print(ans)