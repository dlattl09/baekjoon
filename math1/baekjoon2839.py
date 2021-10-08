# baekjoon problem no.2839
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

import sys

num = int(sys.stdin.readline())

def sugar(N):
  bag = N // 5
  remain = N % 5
  if remain % 3 ==0:
    bag += remain//3
    print(bag)
  else:
    bag = [ i for i in range(bag-1, -1, -1)]
    for minbag in bag:
      remain = N - minbag*5
      if remain % 3 == 0:
        minbag += remain //3
        print(minbag)
        break
    if remain %3 !=0:
      print(-1)   
 
sugar(num)
