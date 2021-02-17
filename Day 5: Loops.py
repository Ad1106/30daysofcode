#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input())
    a=" x "
    b=" = "
    for i in range(1,11):
        print(str(n)+a+str(i)+b+str(n*i))
