

numlist = [0, 0, 1, 1, 2]
num = int(input())

def calc(n):
    tmp = []
    if n%2 == 0:
        tmp.append(numlist[n//2])
    if n%3 == 0:
        tmp.append(numlist[n//3])
    tmp.append(numlist[n-1])
    numlist.append(min(tmp) + 1)

for i in range(5, num+1):
    calc(i)
print(numlist[num])
