#!/bin/python3

import math
import os
import random
import re
import sys



def even(start, n):
    # write your code here
    x=[]
    i=0
    while i<n:
        if start%2==0:
            x.append(start)
            start=start+1
        else:
            x.append(start+1)
            start=start+2
        i=i+1

    return x

if __name__ == '__main__':

    start, n = map(int, input().split())
    res = even(start, n)
    assert type(res) == list
    print(" ".join(map(str, res)) + '\n')
