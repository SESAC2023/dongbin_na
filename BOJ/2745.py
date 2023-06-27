"""
B진법이란?

B가 2인 경우: 0과 1만을 사용해 수를 표현한다.
B가 3인 경우: 0, 1, 2만을 사용해 수를 표현한다.
B가 4인 경우: 0, 1, 2, 3만을 사용해 수를 표현한다.
...

B가 36인 경우: 0, ..., 9까지 그리고 A, ..., Z까지로 수를 표현한다.

예시 1) B = 2, N = 10이라면?
      1      0
    2^1    2^0
따라서 답은 (1 * 2^1) + (0 * 2^0) = 2가 됩니다.

예시 2) B = 2, N = 110이라면?
    1     1     0
  2^2  2^1  2^0
따라서, 답은 (1 * 2^2) + (1 * 2^1) + (0 * 2^0) = 6이 됩니다.

예시 3) B = 3, N = 211이라면?
   2     1      1
 3^2  3^1  3^0
따라서, 답은 (2 * 3^2) + (1 * 3^1) + (1 * 3^0) = 22
0: 000
1: 001
2: 002
3: 010
4: 011
5: 012
6: 020
7: 021
8: 022
9: 100
...

"""

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

""" dictionary 변수
    "0" => 0
    "1" => 1
    ...
    "9" => 9
    "A" => 10
    "B" => 11
    ...
    "Z" => 35
"""
dictionary = dict()
for i in range(10):
    dictionary[str(i)] = i
for i in range(26):
    char = chr(i + ord('A'))  # char는 차례대로 "A"부터 "Z"까지 순회
    dictionary[char] = i + 10

n, b = input().split()  # 입력 문자열 N
b = int(b)  # B진법

n = n[::-1]  # 0제곱부터 보기 위해서 문자열 뒤집기
answer = 0
for i in range(len(n)):  # 각 자리마다 확인하며
    x = dictionary[n[i]]  # 현재 문자열을 수로 바꾼 값
    y = b**i  # 현재 곱해질 수(제곱 수)
    answer += (x * y)
print(answer)
