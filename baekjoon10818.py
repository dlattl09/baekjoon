# baekjoon problem no.108018
# max min of N numbers

numbers = input()
num_array = list(map(int, input().split()))
num_array.sort()
min = num_array[0]
max = num_array[-1]
print(min, max)

