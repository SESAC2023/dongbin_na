n, k = map(int, input().split())

cnt = 0
for hour in range(n + 1):
    for minute in range(60):
        for second in range(60):
            hour = str(hour).zfill(2)
            minute = str(minute).zfill(2)
            second = str(second).zfill(2)
            current = hour + minute + second
            if str(k) in current:
                cnt += 1

print(cnt)
