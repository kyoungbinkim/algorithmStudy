from sys import stdin

def Square(a,b):
    ret = 1
    tmp = a

    for i in bin(b)[2:][::-1]:
        if i == '1':
            ret  = (ret * tmp) % 900528
        tmp = (tmp* tmp) % 900528
    return ret

int2char = {}

string = input()
for i in range(len(string)):
    int2char.update({string[i]:i})
ans = 0
target = stdin.readline().replace('\n','')
ans =int(len(int2char) * (len(int2char) **(len(target)-1) - 1 ) // (len(int2char) - 1)) % 900528
tmp = 1
for i in range(len(target)):
    ans += int2char[target[::-1][i]] * tmp
    ans = ans % 900528
    tmp = tmp * len(int2char) % 900528
print((ans+1)%900528)