# baekjoon problem no.2292
# beehouse

num = int(input())
count = 1
while num > 1:
    num -= (6 * count)
    count += 1
print(count)
