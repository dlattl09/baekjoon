from collections import Counter

words = input()

ascii = []
for i in words:
  ascii.append(ord(i))
ascii_big = [i-32 if i>90 else i for i in ascii]

def modefinder(numbers):
   c = Counter(numbers)
   modes = []
   for num in c.most_common():
      if num[1] == c.most_common()[0][1]:
          modes.append(num[0])
   if len(modes) == 1:
     print(chr(modes[0]))
   else:
     print('?')

modefinder(ascii_big)
