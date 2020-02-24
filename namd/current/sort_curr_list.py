import os
from itertools import chain

f = open('curr_namd_list')
l = f.readlines()

m = []
for i in range(len(l)):
    m.append(l[i].split())

n = list(chain.from_iterable((m)))
n = sorted(n)

f = open('curr_namd_list_sorted','w')
for j in n:
    f.write(j + '\n')
