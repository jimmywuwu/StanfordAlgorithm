from collections import defaultdict
import random

with open('test_case.txt','rb') as f:
    data=f.readlines()

def getf(f, v):
    if f[v] == v:
        return v
    else:
        f[v] = getf(f, f[v])
        return f[v]

def merge(f, v, u):
    t1 = getf(f, v)
    t2 = getf(f, u)
    if t1 != t2 :
        f[t2] = t1

import math
import numpy as np
overall=np.inf
for iter in range(100000):
    f=[i for i in range(200)]
    graph=[]
    node=[]
    v=0
    for i in data:
        line=i.split(' ')
        v+=1
        node.append(int(line[0])-1)
        for j in range(1,len(line)-1):
            graph.append((int(line[0])-1,int(line[j])-1))

    E=len(graph)

    while v>2:
        i=random.randint(0,E-1)
        ## Check if src,target EDGE[i] in the same subset
        subset1=getf(f,graph[i][0])
        subset2=getf(f,graph[i][1])

        ## if the same continue , else contraction
        if subset1==subset2:
            continue
        else:
            merge(f,graph[i][0],graph[i][1])
            v-=1

    minimum_cut=0
    for i in graph:
        subset1=getf(f,i[0])
        subset2=getf(f,i[1])
        if subset1!=subset2:
            minimum_cut+=1
            print(i[0],i[1])
    overall=min(overall,minimum_cut)
    print(iter,': ',overall),minimum_cut






# print(node)
# print(graph)
# while graph node number larger then 2
# 1 pick one edge (random selection,then pop the edge)
# 2 merge node (revised all the source node)





