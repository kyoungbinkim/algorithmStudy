
n = int(input())
while n!=0:
    nbin = bin(n-1)[2:]
    a = []
    cnt = 0
    for s in nbin[::-1]:
        if s == '1':
            a.append(3**cnt)
        cnt +=1
    k = str(a)
    if len(a) == 0:
        print("{ }")
    else:
        print("{ ",end='')
        for tmp in k[1:len(k)-1]:
            print(tmp,end='')
        print(" }",end='\n')
    n=int(input())