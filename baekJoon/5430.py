from sys import stdin

def hi(s):
    ans =[0,0,False]
    for i in range(len(s)):
        if s[i] == 'D':
            if ans[2]:
                ans[1] += 1
            else:
                ans[0] += 1

        elif s[i] == 'R':
            ans[2] = not ans[2]
    return ans

for _ in range(int(stdin.readline())):
    cmd,n = stdin.readline().replace('\n', ''), int(stdin.readline())
    lstr = stdin.readline().replace(","," ").replace('[',"").replace(']','')
    l = list(map(int,lstr.split()))
    cmdList = hi(cmd)
    if sum(cmdList[:2]) > len(l):
        print("error")
    else:
        for _ in range(cmdList[0]):
            l.pop(0)
        for _ in range(cmdList[1]):
            l.pop()
        
        if cmdList[2]:
            l.reverse()
        print(str(l).replace(" ",""))
    