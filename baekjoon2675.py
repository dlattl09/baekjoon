# Baekjoon problem no.2675
# repeated string

total_num = int(input())
for i in range(total_num):
  words = input().split()
  word = words[1]
  num = int(words[0])

  continued = [i for i in word for j in range(num)]
  print(''.join(continued))
