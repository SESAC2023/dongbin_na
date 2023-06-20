hour, minute = map(int, input().split())
c = int(input()) 

hour += c // 60 
minute += c % 60

if minute >= 60:
    hour += 1
    minute -= 60

if hour >= 24:
    hour -= 24

print(hour, minute)
