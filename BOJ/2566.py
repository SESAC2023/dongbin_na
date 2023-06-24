n = 9

arr = [[0] * n for i in range(n)]
"""
[
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0],
]
"""

max_value = -1
max_position = [-1, -1]

# 한 줄(row)씩 입력을 받으며
for i in range(n):
    line = list(map(int, input().split()))
    # 한 열(column)을 하나씩 확인하며
    for j in range(n):
        # 현재 보고 있는 값
        arr[i][j] = line[j]
        # 현재 보고 있는 값이 최댓값을 갱신한다면
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_position = [i, j]

print(max_value)
print(max_position[0] + 1, max_position[1] + 1)

""" 2번 솔루션
arr = []

max_value = -1
for i in range(9):
    arr.append(list(map(int, input().split())))
    for j, x in enumerate(arr[i]):
        if max_value < x:
            max_value = x
            max_index = (i + 1, j + 1)

print(max_value)
print(max_index[0], max_index[1])
"""
