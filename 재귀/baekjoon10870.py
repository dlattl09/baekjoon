# baekjoon problem no.10870
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.


import sys

num = int(sys.stdin.readline())

def fibonacci(n):
  if n <=1:
    return n
  else:
    return fibonacci(n-1)+fibonacci(n-2)

result = fibonacci(num)
print(result)
