#!/bin/python3

import math
import os
import random
import re
import sys


def addToDict(edge):
    nodeOne,nodeTwo = edge.split(",")
    nodeOne = nodeOne[1]
    nodeTwo = nodeTwo[0]
    return (nodeOne , nodeTwo)

def Order(tree,root,s):
    s = s + '(' + str(root)
    if root in tree:
        for node in tree[root]:
            s = Order(tree,node,s)
    s = s + ')'
    return s




def TreeDict(tree,totalTree):
    if " " in tree:
            Edges = tree.split(" ")
    else:
            Edges = list([tree])

    total =  tuple(map(addToDict,Edges));

    for Tree in total:
        if Tree[0] in totalTree:
            totalTree[Tree[0]].append(Tree[1])
        else:
            totalTree[Tree[0]] = list([Tree[1]])

    return totalTree


def DFS(tree,visited,cs):
    visited.append(cs)
    if cs in tree:
        for child in tree[cs]:
            if (child not in visited):
                DFS(tree,visited,child)


def getRoot(tree,root,visited):
    new = ''
    if not root[0]:
        for key in tree:
            if key not in visited:
                new = key
                DFS(tree,visited,key)
    else:
        DFS(tree,visited,root[1])

    return (new,visited)




def getErrors(tree,visited,queue):
    while len(queue) > 0:
        element = queue.pop()
        current = []
        visited.append(element)
        if element in tree:
            for child in tree[element]:
                if child in current:
                    return (False,'E2')

                if child in visited:
                    return (False,'E3')

                current.append(child)
                queue.append(child)

            if len(current) > 2:
                return (False,'E1')


    return (True,'Nothing to worry')



def getdisconnectedComponents(tree,root,nodelist):
    visited = []
    mainroots = []
    mainroots.append(root)
    DFS(tree,visited,root)

    newroot = root
    while newroot != '':
        newroot = getRoot(tree,[False,''],visited)[0]
        if newroot != '':
            mainroots.append(newroot)

    return mainroots


def sExpression(nodes):
    if nodes=="":
        return "E5"
    tree = TreeDict(nodes,dict())
    for key,value in tree.items():
         tree[key].sort()

    gotroot = getRoot(tree,(False,''),[])
    alldisconnected = getdisconnectedComponents(tree,gotroot[0],gotroot[1])
    if len(alldisconnected) > 1:
        b = 'E4'
        for x in alldisconnected:
            visited = []
            queue = [x]
            p = getErrors(tree,visited,queue)
            if not p[0]:
                if p[1] < b:
                    b = p[1]

        return b
    else:
        visited = []
        queue = [gotroot[0]]
        p = getErrors(tree,visited,queue)
        if p[0]:
            return Order(tree,gotroot[0],'')
        else:
            return p[1]


if __name__ == '__main__':
    nodes = input()
    result = sExpression(nodes)
    print(result)
