counter = dict()
data = input()

# 전형적인 카운터(counter) 구현(중요)
for x in data:
    x = x.upper() # 무조건 대문자로 통일
    if x not in counter:
        counter[x] = 1
    else:
        counter[x] += 1

# 가장 많이 사용된 알파벳을 찾기
max_cnt = 0
max_char = "a"
for (key, value) in counter.items():
    if value > max_cnt:
        max_cnt = value
        max_char = key

# 가장 많이 사용된 알파벳이 2개 이상인지 확인
cnt = 0
for (key, value) in counter.items():
    if value == max_cnt:
        cnt += 1

if cnt >= 2:
    print("?")
else:
    print(max_char)
