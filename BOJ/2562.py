n = 9
arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

max_value = -1e9  # 일단 무지막지하게 작은 값
max_index = -1  # 존재할 수 없는 위치

for i in range(n):
    # 현재 원소가 현재까지의 max_value보다 크다면
    if arr[i] > max_value:
        max_value = arr[i]  # 갱신
        max_index = i

print(max_value)
print(max_index + 1)
