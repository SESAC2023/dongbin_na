x, y, z = map(int, input().split())

# 같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금
if x == y and y == z:
    print(10000 + x * 1000)
# x와 y만 같은 경우
elif x == y and x != z:
    print(1000 + x * 100)
# x와 z만 같은 경우
elif x == z and x != y:
    print(1000 + x * 100)
# y와 z만 같은 경우
elif y == z and x != y:
    print(1000 + y * 100)
else:
    print(max(x, y, z) * 100)
