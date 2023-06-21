n = int(input())
arr = list(map(int, input().split()))
v = int(input())

""" 1번 솔루션
print(arr.count(v))
"""

cnt = 0
for i in range(n):
    if arr[i] == v:
        cnt += 1
print(cnt)
