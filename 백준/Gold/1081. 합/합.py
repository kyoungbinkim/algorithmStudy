
l, u = map(int ,input().split())

def calcSum(n):
    if n<0:
        return 0
    sum = 0
    digit = len(str(n))
    ten = 10 ** (digit-1)

    l, num, r = 0, n//ten, n%ten

    while ten >0:
        sum += l * 45 * ten
        sum += (r+1) * num
        sum += (num * (num-1) //2)  * (ten )
        
        ten = ten // 10
        if ten == 0:
            break
        l = l * 10 + num 
        num = r // ten
        r = r % ten
    return sum

print(calcSum(u) - calcSum(l-1))
