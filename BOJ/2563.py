n = 100  # 도화지 크기

# 전체 도화지 정보
arr = []
for i in range(n):
    line = [0] * n
    arr.append(line)

m = int(input())  # 색종이 수
for i in range(m):
    x, y = map(int, input().split())
    # 맵을 벗어나지 않으므로, x, y는 [0, 90]
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            arr[j][k] = 1

area = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1: area += 1
print(area)
