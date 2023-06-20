x = int(input())
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    x = x - (a * b)

# 정확히 0이 된다면 가격이 일치하는 것
if x == 0:
    print("Yes")
else:
    print("No")
