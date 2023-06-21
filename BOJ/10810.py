n, m = map(int, input().split())

arr = [0] * n

for _ in range(m):
    left, right, value = map(int, input().split())
    # left부터 right까지 value를 채워넣기
    for i in range(left - 1, right):
        arr[i] = value

for x in arr:
    print(x, end=" ")
