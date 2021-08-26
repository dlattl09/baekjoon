# Baekjoon problem no.2908
# comparison

numbers = input().split()
num1 =numbers[0][::-1]
num2 = numbers[1][::-1]

if int(num1)>int(num2):
  print(num1)
else:
  print(num2)
