from sys import stdin

n = int(stdin.readline())

def isPrime(num):
    if num == 2 or num == 3:
        return True
    elif num == 1 or num % 2 == 0:
        return False    
    
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

def isPalindrome(num):
    num = str(num)
    for i in range(len(num)//2):
        if num[i] != num[-1-i]:
            return False
    return True

while not isPrime(n) or not isPalindrome(n):
    n += 1
print(n)