#!/bin/python3

import math
import os
import random
import re
import sys
import json
from urllib.request import urlopen
import datetime


#
# Complete the 'numDevices' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING statusQuery
#  2. INTEGER threshold
#  3. STRING dateStr
#

def numDevices(statusQuery, threshold, dateStr):
    # Write your code here
    url_given="https://jsonmock.hackerrank.com/api/iot_devices/search?status={}"
    url=url_given.format(statusQuery)
    json_url = urlopen(url)
    data1 = json.loads(json_url.read())
    x=data1['total_pages']
#     y=data1['total']
    z=data1['page']
    r=0
#     print(data1)
    while z<=x:
        url_given="https://jsonmock.hackerrank.com/api/iot_devices/search?status={0}&page={1}"
        url=url_given.format(statusQuery,z)
        json_url = urlopen(url)
        data1 = json.loads(json_url.read())
        for j in range(len(data1['data'])):
            p = datetime.datetime.fromtimestamp((data1['data'][j]['timestamp'])/1000.0)
            p=p.strftime('%m-%Y')
            if data1['data'][j]['operatingParams']['rootThreshold']>threshold:
                if p == dateStr:
                    r=r+1
        z=z+1



    return r

if __name__ == '__main__':

    statusQuery = input()

    threshold = int(input().strip())

    dateStr = input()

    result = numDevices(statusQuery, threshold, dateStr)

    print(result)
