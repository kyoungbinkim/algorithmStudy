from sys import stdin
from copy import deepcopy
p = 998_244_353
rl = stdin.readline
base = [
            [1,0,0,0,1],
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,0]
      ]
      
def matMul(a,b):
      ret = [[0 for _ in range(5)] for _ in range(5)]
      
      for i in range(5):
            for j in range(5):
                  for k in range(5):
                        ret[i][j] += a[i][k] * b[k][j]
                        ret[i][j] = ret[i][j] % p
      return ret

def matPow(m=base, b=0):
      ret = [[int(i==j) for i in range(5)] for j in range(5)]
      sq = deepcopy(m)
      for c in bin(b)[2:][::-1]:
            if c == '1':
                  ret = matMul(ret, sq)
            
            sq = matMul(sq, sq)
      return ret

for _ in range(int(rl())):
      n = int(rl())
      tmp = [1,1,1,2,2]
      if n <= 5:
            print(tmp[n-1])
      else:
            r = matPow(base, n-5)
            ans = 0
            for i in range(5):
                  ans += tmp[4-i] * r[0][i]
                  # ans = p
                  # print(ans )
            print(ans % p)
      