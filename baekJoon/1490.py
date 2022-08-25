from gettext import dgettext


def check(num, numList):
    for n in numList:
        if num % n != 0:
            return False
    return True

numStr = input()
numList = []

for n in numStr:
    if n == '0' or int(n) in numList:
        continue
    numList.append(int(n))

i=0
degree=1
tmp = numStr
while not check(int(tmp), numList):
    tmp = numStr + str(i).zfill(degree)
    i+=1
    if i == (10**degree):
        if check(int(tmp), numList):
            break
        i = 0
        degree += 1
        tmp = numStr + str(i).zfill(degree)

print(tmp)


