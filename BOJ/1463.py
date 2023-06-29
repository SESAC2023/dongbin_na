"""
import sys

sys.setrecursionlimit(int(1e6))

# 하향식(재귀 함수) 풀이 방법: 3단계로 해결
# 1부터 1,000,000까지의 수에 대하여 "1로 만들기 위한 최소 연산"
d = [0] * (int(1e6) + 1)  # DP 테이블


def dp(x):
    if x == 1:  # (1) 종료 조건
        return 0
    if d[x] != 0:  # x에 대하여 계산한 적이 있다면
        return d[x]
    # (2) 점화식에 따라 계산 d[x] = min(d[x-1], d[x//2], d[x//3]) + 1
    current = dp(x - 1) + 1
    if x % 2 == 0:
        current = min(current, dp(x // 2) + 1)
    if x % 3 == 0:
        current = min(current, dp(x // 3) + 1)
    # (3) 계산한 결과를 DP 테이블에 기록하고, 반환
    d[x] = current
    return d[x]


n = int(input())
print(dp(n))
"""

# 점화식은 d[x] = min(d[x-1], d[x//2], d[x//3]) + 1

n = int(input())

d = [0] * (int(1e6) + 1)  # DP 테이블

for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)

print(d[n])
