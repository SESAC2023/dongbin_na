"""
약수의 성질: 약수는 대칭 관계를 가진다.
예시) 32의 약수 = [1, 2, 4, 8, 16, 32]

32 = 1 X 32
32 = 2 X 16
32 = 4 X 8
(대칭)
32 = 8 X 4
32 = 16 X 2
32 = 32 X 1

따라서, 중간 값(median)까지만 보면 된다.
즉, n이 주어졌을 때, sqrt(n)까지만 보면 된다.

그러면 N이 최대 10,000,000이므로, 1부터 sqrt(n)까지 보면서
최대한 많이 나누면 되는 거 아닌가? => 시간 초과 안 받음

sqrt(n)은 약 3,000이라고 두고, log N은 대충 23이라고 두면 되므로
해봤자 69,000 이니까 시간 초과 X
"""

import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n = int(input())

is_prime = True
# 제곱근까지만 보면서, 가능하면 계속 나누기
for i in range(2, n): # 제곱근까지 안 봐도 시간 초과 안 나면... 이렇게
    # 나누어 떨어지는 경우, 안 나누어 떨어질 때까지 계속 나누기
    # 이것을 우리는 소인수 분해라고 한다
    while n % i == 0:
        print(i)
        is_prime = False
        n = n // i  # n을 i로 나누도록 하기

# 만약에 소수였으면, 한 번도 출력이 안 됐을 것임.
# 따라서, 소수일 때에 한해서만 N을 그대로 출력
if is_prime:
    print(n)
