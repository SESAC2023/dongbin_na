"""
X = 10,000,000 이므로, 2차원 배열에 표현하려면 → 바로 메모리 초과
따라서, 단순 시뮬레이션으로는 해결할 수 없다.

이런 문제는 보자마자, "무언가 수학적인 솔루션, 무언가 아이디어가 있겠다!"

실버 수준 => 이런 문제는 보통 규칙성 찾기로 풀림
=> 수능 수학 29번 중에서 노가다 문제 느낌

1단계: 길이가 1 => 1/1                                     X = {1}
2단계: 길이가 2 => 1/2, 2/1 (정방향)                    X = {2, 3}
3단계: 길이가 3 => 3/1, 2/2, 1/3 (역방향)              X = {4, 5, 6}
4단계: 길이가 4 => 1/4, 2/3, 3/2, 4/1 (정방향)        X = {7, 8, 9, 10}
5단계: 길이가 5 => 5/1, 4/2, 3/3, 2/4, 1/5 (역방향)  X = {11, 12, 13, 14, 15}

1) 현재 X가 몇 단계에 속하는지
2) 현재 단계가 정방향(분모가 큰 것부터 출발)인지, 역방향인지 찾아서 정답 도출
  * 짝수면 정방향, 홀수면 역방향

예시) X = 13이라고 해볼게요.
  = X는 5단계에 속해 있다. 왜냐? 가장 가까운 누적 개수가 4단계(10개)이니까.
  = 5단계에서 3번째 수라는 걸 알기에, 5단계가 역방향이니까 5/1, 4/2, 3/3 => 즉, 3/3이 정답
"""

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

x = int(input())

# 단계 찾기
summary = 1  # 누적 길이
stage = 1  # 단계(stage)
while True:
    summary += stage
    if summary > x:
        break
    stage += 1

# X가 몇 단계인지 계산 완료
# print("단계:", stage)
# print("누적 길이:", summary)
# print("현재 단계에서 몇 번째인가:", x - (summary - stage) + 1)

forward = True  # 정방향 여부
if stage % 2 == 1:  # 홀수라면
    forward = False

if forward:  # 정방향이라면
    a = 1  # 분자
    b = stage  # 분모
    for i in range(x - (summary - stage)):
        a += 1
        b -= 1
else:
    a = stage  # 분자
    b = 1  # 분모
    for i in range(x - (summary - stage)):
        a -= 1
        b += 1

print(str(a) + "/" + str(b))
