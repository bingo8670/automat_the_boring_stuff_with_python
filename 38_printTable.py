#-*- coding: UTF-8 -*-
tableDate=[['apples', 'oranges', 'cherries', 'banana'],
           ['Alice', 'Bob', 'Carol', 'David'],
           ['dogs', 'cats', 'moose', 'goose']]
def findmaxlen(Dates):
    maxlen=0
    for i in range(len(Dates)):
        if len(Dates[i])>maxlen:
            maxlen=len(Dates[i])
    return maxlen
#print(findmaxlen(tableDate[0]))
def printTable(List):
    k=len(List)#列表的个数
    v=len(List[0])#列表中元素的个数
    for i in range(v):
        for j in range(k):
            print(List[j][i].rjust(findmaxlen(List[j])), end=' ')
        print()
printTable(tableDate)
