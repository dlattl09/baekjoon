# Baekjoon problem no.2577
# counting prob

num1 = input()
num2 = input()
num3 = input()

num3 = int(num1) * int(num2) * int(num3)

ans = list(str(num3))

for i in range(10):
        print(ans.count(str(i)))
