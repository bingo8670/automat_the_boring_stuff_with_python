# -*- coding: utf-8 -*-

import os

spamList = []
fullList = []

for file in os.listdir('.'):
    if file.startswith('spam') and file.endswith('txt'):
        spamList.append(file)

#把列表从小到大排序，这个列表是不完整的，缺失了一些元素。
spamList.sort()

#找到列表最后一个元素对应的数值，以这个数值为长度，创建一个完整的列表。
finalNum = int(spamList[-1][5:-4])
for i in range(1, finalNum+1):
    fileNum = str(i).zfill(3)
    #zfill的作用是给1、2、3前面补上0。
    fullList.append('spam' + fileNum + '.txt')

#寻找spamList不存在，而fullList中存在的元素。
diffList = list(set(fullList).difference(set(spamList)))

#spamList倒序，从后往前，改为diffList的名字。
for i in range((len(diffList) * -1), 0):
    os.rename(spamList[i], diffList[i])
