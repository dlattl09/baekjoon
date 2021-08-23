# Baekjoon problem no.4344
# caculate i>mean_value

case_num = int(input())
for i in range(case_num):
  score = input()
  score = score.split()
  score = [int(i) for i in score]

  avg = sum(score[1:], 0)/score[0]
  num = 0
  for i in score[1:]:
    if i > avg:
      num += 1
  print('%0.3f' % ((num/score[0])*100) + '%')
