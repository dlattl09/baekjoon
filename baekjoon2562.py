# baekjoon problem no.2562
# finding max and it's index

import copy

original_array = []
for i in range(9):
	original_array.append(int(input()))

sorted_array = copy.deepcopy(original_array)
sorted_array.sort()
print(sorted_array[-1])
print(original_array.index(sorted_array[-1])+1)
