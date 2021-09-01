# baekjoon problem no.1316
# 그룹 단어 체커

import sys
n = int(sys.stdin.readline().rstrip())
data = [sys.stdin.readline().strip() for i in range(n)]


not_group = 0
for word in data:
  b = list(word)
  check = []
  check.append(b.pop())
  i=0
  while(1):
    if len(b)==0:
      break
    popped = b.pop()  
    if popped == check[i]: 
      check.append(popped)
      i+=1   
    else:
      if popped not in check:
        check.append(popped)
        i+=1     
      else:
        not_group+=1       
        break
print(n-not_group)
