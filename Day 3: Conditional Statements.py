#!/bin/python3

import math
import os
import random
import re
import sys

N = int(input())
if(N%2==1):
    print("Weird")
elif(N%2==0):
    if(N>=2 and N<=5):
        print("Not Weird")
    elif(N>=6 and N<=20):
        print("Weird")
    elif(N>20):
        print("Not Weird")