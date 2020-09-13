#!/bin/python3

import math
import os
import random
import re
import sys
import json
from urllib.request import urlopen




def getUsernames(threshold):
    # Write your code here

    url="https://jsonmock.hackerrank.com/api/article_users?page=1"

    json_url = urlopen(url)
    data1 = json.loads(json_url.read())
    x=data1['total_pages']
    z=1
    r=[]

    while z<=x:
        url_given="https://jsonmock.hackerrank.com/api/article_users?page={}"
        url=url_given.format(z)
        json_url = urlopen(url)
        data1 = json.loads(json_url.read())
        for j in range(len(data1['data'])):
            if data1['data'][j]['submission_count']>threshold:
                r.append(data1['data'][j]['username'])

        z=z+1
    return r

if __name__ == '__main__':

    threshold = int(input().strip())

    result = getUsernames(threshold)
    for i in range(len(result)):
        print(result[i])
