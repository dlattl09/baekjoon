# Baekjoon problem no.4673
# self number

import copy

def dn(num):
  dnum = copy.deepcopy(num)
  for i in str(num):
    dnum += int(i)
  return dnum

def self_number(max_num):
  collection = [i for i in range(1,max_num+1)]
  for i in range(1,max_num+1):
    if dn(i) in collection:
      collection.remove(dn(i))
  for j in collection:
    print(j)

self_number(10000)
