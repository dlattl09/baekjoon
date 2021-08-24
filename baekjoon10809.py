# Baekjoon problem no.10809
# finding alphabet

word = input()
alphabet ='abcdefghijklmnopqrstuvwxyz'  

location = []
for x in alphabet :
    location.append(str(word.find(x)))
    
print(' '.join(location))


