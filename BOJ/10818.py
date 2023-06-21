n = int(input())
arr = list(map(int, input().split()))

min_value = 1e9 # 일단 무지막지하게 큰 값
max_value = -1e9 # 일단 무지막지하게 작은 값

for i in range(n):
    # 현재 원소가 현재까지의 min_value보다 작다면
    if arr[i] < min_value:
        min_value = arr[i] # 갱신
    # 현재 원소가 현재까지의 max_value보다 크다면
    if arr[i] > max_value:
        max_value = arr[i] # 갱신

print(min_value, max_value)
