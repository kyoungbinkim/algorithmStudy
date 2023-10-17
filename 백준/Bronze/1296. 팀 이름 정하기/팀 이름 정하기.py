


seq = ['L', 'O', 'V', 'E']

def calcLOVE(name:str):
    ret = []
    for i in range(4):
        ret.append(name.count(seq[i]))
    return ret

def calcScore(name1, name2):
    s = [name1[i] + name2[i] for i in range(4)]

    score = 1
    for i in range(3):
        for j in range(i+1, 4):
            score *= (s[i] + s[j])

            score %= 100
    return score

myName  = input()
myScore = calcLOVE(myName)

ans, ansScore = 'z'*20, 0
for _ in range(int(input())):
    tmp = input()
    tmpScore = calcScore(calcLOVE(tmp), myScore)

    if tmpScore > ansScore or (tmpScore == ansScore and ans>tmp):
        ansScore = tmpScore
        ans = tmp
print(ans)
