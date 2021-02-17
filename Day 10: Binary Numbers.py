#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    l=[]
    c=1
    b=1
    p=int((bin(n).replace("0b","")))
    while (p>0):
        b=p%2
        l.append(b)
        p=p//10
    for i in range (1,len(l)):
            if(l[i-1]==l[i] and l[i]==1):
                c=c+1
            elif(c>b):
                b=c
            if(l[i]==0):
                c=1
    if(c>b):
        b=c
    print(b)
 
