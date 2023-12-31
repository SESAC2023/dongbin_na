"""
<경우의 수>
1) 순열: itertools.permutation()
  - N개의 원소 리스트에서 중복 없이 M개를 골라 만든 수열
  - N개에서 M개를 고르기 (순서가 다르면 다른 경우)
2) 조합: itertools.combination()
  - N개의 원소 리스트에서 중복 없이 M개를 골라 만든 수열
  - 순서가 달라도 원소가 동일하면 같은 경우
3) 중복 순열: itertools.product()
  - N개의 원소 리스트 중에서 중복을 허용해서 M개를 골라 만든 수열
  - N개에서 M개를 고르기 (순서가 다르면 다른 경우)
4) 중복 조합: itertools.combinations_with_replacement()
  - N개의 원소 리스트에서 중복을 허용해서 M개를 골라 만든 수열
  - 순서가 달라도 원소가 동일하면 같은 경우
→ 실전 코딩, 카카오 코테에서는 사용 가능
→ 삼성전자 코테에서는 사용 못 하게 막는 경우가 있다고 함
  - 그래서 짤 수 있어야 함
"""

import sys

sys.setrecursionlimit(int(1e6))

n = int(input())
data = list(map(int, input().split()))  # [3, 4, 5]
operators = list(map(int, input().split()))  # [+개수, -개수, *개수, /개수]
m = n - 1  # 선택할 총 연산자 수

selected = []  # 현재 경우에서 선택된 원소들

min_value = 1e10
max_value = -1e10


# depth: 현재 재귀에서 선택된 원소의 개수
def dfs(depth):
    global min_value, max_value
    if depth == m:
        # 실제로 현재 경우에 대하여 처리하는 부분
        total = data[0]
        for i in range(m):
            current = selected[i]
            if current == 0:  # 더하기
                total += data[i + 1]
            elif current == 1:  # 빼기
                total -= data[i + 1]
            elif current == 2:  # 곱하기
                total *= data[i + 1]
            else:  # 나누기
                if total < 0:
                    total = -((-total) // data[i + 1])
                else:
                    total //= data[i + 1]
        min_value = min(min_value, total)
        max_value = max(max_value, total)
        return
    for i in range(4):
        if operators[i] == 0:
            continue
        # 해당 연산자가 아직 더 쓰일 수 있다면
        # 백트래킹은 3단계로 재귀 호출
        # (1) 원소 넣기
        operators[i] -= 1
        selected.append(i)
        # i == 0은 '+', i == 1은 '-', i == 2는 '*', i == 3은 '/'
        dfs(depth + 1)  # (2) 재귀 호출
        # (3) 원소 빼기
        operators[i] += 1
        selected.pop()


dfs(0)
print(max_value)
print(min_value)
