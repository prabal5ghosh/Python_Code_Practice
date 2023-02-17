from os import *
from sys import *
from collections import *
from math import *



def sumOrProduct(n, q):
    que = q
    if que == 1:
        s=0
        for i in range(n+1):
            s=s+i
        return s

    if que == 2:
        s=1
        for i in range(1,n+1):
            s=s*i
        M = 1000000007
        for i in range(1, s + 1):
            s = (s * i) % M
            return s



    # Write your Code here.
print(sumOrProduct(4, 2))