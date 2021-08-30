# Baekjoon problem no.2941
# 크로아티아 알파벳

import re
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in cro:
  word = word.replace(i, '!')
print(len(word))
