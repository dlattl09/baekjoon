# Baekjoon problem no.8958
# O/X quiz

prob_num = int(input())
for problem in range(prob_num):
  num = 0
  continued = 1
  for data in problem:
    if data =='O':
      num += continued
      continued += 1
    else:
      continued = 1
  print(num)
