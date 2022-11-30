from sys import stdin

def calc(nlist):
    ansMap = {}
    for num in nlist:
        # tmp = ansMap.copy()
        updateList = []
        for k in ansMap.keys():
            if ansMap.get(k) == None:
                updateList.append([k+num, 1])
            else:
                updateList.append([k+num, ansMap[k]])
        
        for update in updateList:
            if ansMap.get(update[0]) == None:
                ansMap.update({update[0] : update[1]})
            else:
                ansMap[update[0]] += update[1]

        if ansMap.get(num) == None:
            ansMap.update({num : 1})
        else:
            ansMap[num] += 1
    return ansMap
    
answer = 0
size, tar = map(int, stdin.readline().split())
nlist = list(map(int, stdin.readline().split()))

nlist.sort()
A = nlist[:size//2]
B = nlist[size//2:]

Aans = calc(A)
Bans = calc(B)


#print(Aans,Bans)
if Bans.get(tar) != None:
    answer = Bans[tar]
    # if Aans.get(0) != None:
    #     answer += Bans[tar] * Aans[0]

for ak in Aans.keys():
    if ak == tar:
        answer += Aans[ak] 
        if Bans.get(0) != None:
            answer += Bans[0] * Aans[ak]
        continue
    if Bans.get(tar-ak) == None:
        continue
    answer += Aans[ak] * Bans[tar-ak]
print(answer)


