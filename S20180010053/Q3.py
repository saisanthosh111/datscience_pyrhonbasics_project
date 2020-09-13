#!/bin/python3

import math
import os
import random
import re
import sys



class IncreasingList:
    x=[]
    def append(self, val):
        """
        first, it removes all elements from the list that have greater values than val, starting from the last one, and once there are no greater element in the list, it appends val to the end of the list
        """

        for i in reversed(self.x):
            if i>val:

                self.x.pop(self.x.index(i))


        self.x.append(val)


    def pop(self):
        """
        removes the last element from the list if the list is not empty, otherwise, if the list is empty, it does nothing
        """
        if len(self.x)!=0:
            self.x.pop()


    def __len__(self):
        """
        returns the number of elements in the list
        """
        # print(self.x)
        r=len(self.x)
        return r
if __name__ == '__main__':
    lst = IncreasingList()
    q = int(input())
    for _ in range(q):
        op = input().split()
        op_name = op[0]
        if op_name == "append":
            val = int(op[1])
            lst.append(val)
        elif op_name == "pop":
            lst.pop()
        elif op_name == "size":
            print(len(lst))
        else:
            raise ValueError("invalid operation")
