# baekjoon problem no.2447
# 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.


import sys

num = int(sys.stdin.readline())
def box(n):
    if n == 3:
        return ['***','* *','***']

    drawing = box(n//3)
   # print(drawing)
    side_array = []
    mid_array = []
    results = []
    for i in range (int(n/3)):
      side = drawing[i]*3
      mid = drawing[i] + ' '*(int(n/3)) + drawing[i]
      side_array.append(side)
      mid_array.append(mid)

    results.extend(side_array)
    results.extend(mid_array)
    results.extend(side_array)
    return results
for i in box(num):
  print(i)
