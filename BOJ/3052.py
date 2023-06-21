""" 1번 솔루션
arr = []

for i in range(10):
    x = int(input())
    arr.append(x % 42)

print(len(set(arr)))
"""

data = set()

for i in range(10):
    x = int(input())
    data.add(x % 42)

print(len(data))
