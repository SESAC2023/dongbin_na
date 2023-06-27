"""
임의의 크기를 가지는 M X N 크기의 보드가 있다.

체스판의 크기는 항상 8 X 8 이잖아요?
목표: 8 X 8의 체스판을 얻는 것
→ 원하는 위치에서 체스판을 뽑아낸 뒤에, 최소한의 정사각형을 다시 색칠하는 것이 목표
"""

import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

row_1 = "WBWBWBWB"
row_2 = "BWBWBWBW"

# 가능한 체스판 형태 1
board_1 = [
    row_1, row_2, row_1, row_2, row_1, row_2, row_1, row_2
]
# 가능한 체스판 형태 2
board_2 = [
    row_2, row_1, row_2, row_1, row_2, row_1, row_2, row_1
]

m, n = map(int, input().split())

arr = []
for i in range(m):
    arr.append(input())

answer = int(1e9) # 가능한 큰 값(왜냐? 최솟값을 찾을 거니까.)
# 가능한 모든 위치에서 확인
for i in range(m - 7): # 행
    for j in range(n - 7): # 열
        # [i, j]부터 [i + 8, j + 8]까지의 정사각형 공간에 대하여
        # "일치하지 않는 위치의 개수를 구하기 = 칠해야하는 개수"
        
        # 체스판 1번
        cnt = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # 불일치하는 경우 카운트 세기
                if arr[x][y] != board_1[x - i][y - j]:
                    cnt += 1 
        answer = min(answer, cnt) # 최솟값 계산
        
        # 체스판 2번
        cnt = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                # 불일치하는 경우 카운트 세기
                if arr[x][y] != board_2[x - i][y - j]:
                    cnt += 1 
        answer = min(answer, cnt) # 최솟값 계산

print(answer)

# 시간 복잡도: O(N * M * 8 * 8) = O(NM) => 시간 초과 x
