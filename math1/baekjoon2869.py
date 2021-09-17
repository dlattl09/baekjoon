# baekjoon problem no.2869
# 첫째 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어진다. (1 ≤ B < A ≤ V ≤ 1,000,000,000)


import sys
import math

a,b,v = map(int, sys.stdin.readline().split())
print(math.ceil((v-b)/(a-b)))
