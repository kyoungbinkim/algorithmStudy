from sys import stdin

n,k = map(int ,stdin.readline().split())
nbin = bin(n)[2:]
cnt = 0
# print( nbin,sum(list(map(int, nbin))))

if sum(list(map(int, nbin))) <= k:
    print('0')
else:
    for i in range(len(nbin)):
        if nbin[i] == '1':
            cnt += 1
        if cnt == k:
            cnt = i
            ans = 2**(len(nbin)-cnt) - int(nbin[i:],2)
            print(2**(len(nbin)-cnt) - int(nbin[i:],2))
            break
