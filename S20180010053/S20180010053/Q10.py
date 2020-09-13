# !/bin/python3

import math
import os
import random
import re
import sys

def countPatterns(n):
    x=(24**n)-(9*(8**n))+(18*(3**n))+(9*(2**n))-24
    return x
if __name__ == '__main__':
    n = int(input().strip())
    result = countPatterns(n)
    print(result)
