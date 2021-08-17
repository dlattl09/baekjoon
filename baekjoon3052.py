#baekjoon problem no.3052
# divide

original_array = []
for i in range(10):
	original_array.append(int(input()))

divided_array = [i%42 for i in original_array]
print(len(set(divided_array)))
