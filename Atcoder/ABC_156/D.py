from operator import mul
from functools import reduce
import math

n,a,b = list(map(int,input().split()))

def pow(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans

def mina(n,a):
  X = math.factorial(n) // math.factorial(a)
  Y = math.factorial(a)