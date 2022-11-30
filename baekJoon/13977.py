from sys import stdin
import math

PRIME = 1000000007

def binomialCoefficient(n,k):
    if k<0 or k>n:
        return 0
    if n-k < k:
        k = n-k
    
    