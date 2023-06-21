"""
[1, 2, 3, 4, 5]
left = 1, right = 2 => [2, 1, 3, 4, 5]
left = 3, right = 4 => [2, 1, 4, 3, 5]
left = 1, right = 4 => [3, 4, 1, 2, 5]
left = 2, right = 2 => [3, 4, 1, 2, 5]
"""

""" 1번 솔루션
n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for i in range(m):
    left, right = map(int, input().split())
    left -= 1
    arr[left:right] = reversed(arr[left:right])

for x in arr:
    print(x, end=" ")
"""

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

for i in range(m):
    left, right = map(int, input().split())
    left -= 1
    temp = []
    for j in range(left, right):
        temp.append(arr[j])
    for j in range(left, right):
        arr[j] = temp.pop()

for x in arr:
    print(x, end=" ")
