# Baekjoon problem no.1065
# Han number

def sequence():
  num = input()
  han_num = 0
  for i in range(1, int(num)+1):
    if i < 100:
      han_num += 1
    elif int(str(i)[2]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[0]):
      han_num += 1
  return han_num

print(sequence())
