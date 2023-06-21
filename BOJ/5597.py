arr = [False] * 31

# arr[0] = False
# arr[1] = False
# ...
# arr[30] = False

for i in range(28):
    x = int(input())
    arr[x] = True  # 제출함

for i in range(1, 31):
    # 제출 안 한 사람 출력
    if arr[i] == False:
        print(i)
