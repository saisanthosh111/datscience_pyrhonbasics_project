#!/bin/python3

import math
import os
import random
import re
import sys



def multiply(a, b, bound):

    # write your code here
    if a*b<=bound:
        return a*b
    else:
        raise ValueError("multiplication of {} and {} with bound {} not possible".format(a,b,bound))


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        a, b, bound = list(map(int, input().split()))
        try:
            res = multiply(a, b, bound)
            print(res)
        except ValueError as e:
            print(e)
