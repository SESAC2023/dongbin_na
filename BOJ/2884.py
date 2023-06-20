hour, minute = map(int, input().split())

minute = minute - 45
# 만약 분(minute)이 45보다 작았다면
if minute < 0:
    minute = minute + 60
    hour = hour - 1
    # 만약 시(hour)가 0이었다면
    if hour < 0:
        hour = 23

print(hour, minute)
