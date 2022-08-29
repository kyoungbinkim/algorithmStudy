from sys import stdin

def isPalindrome(list):
    lenList = len(list)
    for i in range(lenList//2):
        if list[i] != list[lenList-i-1]:
            return False,i, lenList-i-1
    return True, None, None

for i in range(int(stdin.readline())):
    strList = [x for x in stdin.readline().replace('\n','')]
    flag, ind1, ind2= isPalindrome(strList)
    if flag:
        print(0)
        continue
    tmp = strList.copy()
    del strList[ind1]
    del tmp[ind2]
    f1,_,_ = isPalindrome(tmp)
    f2,_,_ = isPalindrome(strList)
    if f1 or f2:
        print(1)
        continue
    print(2)
