#!/bin/python3

import math
import os
import random
import re
import sys
import json
from urllib.request import urlopen


def getArticleTitles(authorN):
    url_given="https://jsonmock.hackerrank.com/api/articles?author={}"
    url=url_given.format(authorN)
    json_url = urlopen(url)
    data1 = json.loads(json_url.read())
    x=data1['total_pages']
    z=data1['page']
    r=[]
#     print(data1)
    while z<=x:
        url_given="https://jsonmock.hackerrank.com/api/articles?author={0}&page={1}"
        url=url_given.format(authorN,z)
        json_url = urlopen(url)
        data1 = json.loads(json_url.read())
        for j in range(len(data1['data'])):
            if data1['data'][j]['author'] == authorN:
                if (data1['data'][j]['title']==None) and (data1['data'][j]['story_title']==None):
                    break
                elif data1['data'][j]['title'] == None:
                    r.append(data1['data'][j]['story_title'])
                elif data1['data'][j]['story_title']==None:
                    r.append(data1['data'][j]['title'])


        z=z+1

    return r
    # Write your code here
if __name__ == '__main__':
    author = input()
    result = getArticleTitles(author)
    print('\n'.join(result))
