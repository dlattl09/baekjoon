# Baekjoon problem no.11654
# Ascii code

def ascii():
  integer = [str(i) for i in range(10)]
  ascii_code = 0
  word = input()
  if word in integer:
    ascii_code = int(word) + 48
  else:
    ascii_code = ord(word)
  return ascii_code

print(ascii())
