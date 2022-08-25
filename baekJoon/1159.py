from sys import stdin
rl = stdin.readline

Dict = {}

for _ in range(int(rl())):
    tmp = rl().replace('\n','')
    if Dict.get(tmp[0]) == None:
        Dict.update({tmp[0]:1})
    else:
        Dict[tmp[0]]+=1
keyList = list(Dict.keys())
keyList.sort()
ans =""
for k in keyList:
    if Dict[k] >= 5:
        ans += k
if ans == "":
    print("PREDAJA" )
else:
    print(ans)