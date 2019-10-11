#!/usr/bin/python
#-*-coding:utf-8-*-
from collections import Counter
all = []
list1 = []
list2 = []
with open('3.txt', 'r') as f:
	lines = f.readlines()
	for line in lines:
		all.append(line.split())
for l in all:
    list1 += [l[1]]
    list2 += [l[6]]
stat_A = Counter(list1)
stat_D = Counter(list2)
print('对A的统计：')
print(stat_A,)
print('对D的统计：')
print(stat_D)


