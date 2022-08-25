import math
def A(num,n):
    return math.floor(math.log(num/n) * n)

def B(num,n):
    return math.ceil((num **(1/n))*n)


num = int(input())
before = A(num,1)
i=2
while True:
    tmp = A(num,i)
    print(i,tmp,before)
    if tmp<before:
        break
    before = tmp
    i+=1
Aans = i-1

before = B(num, 1)
i=2
while True:
    tmp = B(num,i)
    print(i,tmp,before)
    if tmp>=before:
        break
    before = tmp
    i+=1
Bans = i-1
print(Aans, Bans)
