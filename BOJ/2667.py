#DFS와 BFS

import sys
from collections import deque

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

n = int(input())
"""
[
  [0, 1, 1, 0, 1, 0, 0],
  [0, 1, 1, 0, 1, 0, 1],
  [1, 1, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 1, 1],
  ...
]
"""
graph = []
for i in range(n):
    line = input().strip()
    current = []
    for x in line:
        current.append(int(x))
    graph.append(current)

visited = [[False] * n for i in range(n)]

# print(graph)

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 1) 방문 처리 안 된 노드 발견시, 처음 DFS 들어갈 때만 "카운트"
# 2) DFS는 재귀 함수로 상, 하, 좌, 우 이동하면서 전부 방문 처리만


# (x, y)에서 출발해서 도달 가능한 모든 공간에 대해서 "방문 처리"
def dfs(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    # 모든 노드는 인접 노드로 상, 하, 좌, 우 4개를 가진다.
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 이때 (nx, ny)가 인접 노드
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 0:
            continue
        # 여기까지 왔으면, 실제로 존재하는 공간
        if not visited[nx][ny]:
            dfs(nx, ny)


answer = 0
answer_list = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0:
            continue
        # 아직 방문하지 않은 노드라면(아직 탐방하지 않은 연결 요소라면)
        if not visited[i][j]:
            # 해당 노드에서 출발해서 연결 요소 찾기(방문 처리 몽땅)
            answer += 1
            cnt = 0
            dfs(i, j)
            answer_list.append(cnt)

print(answer)
answer_list.sort()
for x in answer_list:
    print(x)
