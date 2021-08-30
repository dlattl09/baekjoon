# Baekjoon problem no.5622
# dial 

word = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 

dial = 0
time = 0
for i in word:
  dial = alphabet.find(i)
  if dial < 18:
    time += dial//3 + 3
  else:
    if dial ==18:
      time += 8
    elif dial <22:
      time += 9
    else :
      time += 10
print(time)
