import sys
from collections import deque
# 재귀 함수 깊이 해제
sys.setrecursionlimit(int(1e6))
# 입력이 10만 줄 이상일 때, 빠르게 입력 받기 위해 사용
input = sys.stdin.readline

# 정점의 개수(n), 간선의 개수(m), 시작 정점(v)
n, m, v = map(int, input().split())

graph = [[] for i in range(n + 1)]  # 그래프
visited = [False] * (n + 1)  # 방문 처리 배열

for i in range(m):
    x, y = map(int, input().split())
    # 양방향 간선
    graph[x].append(y)
    graph[y].append(x)

# 방문할 때는 오름차순으로 방문
for i in range(1, n + 1):
    graph[i].sort()


def dfs(x):
    visited[x] = True  # 방문 처리
    print(x, end=" ")
    for y in graph[x]:  # 인접한 노드
        # 방문 안 했다면 스택에 넣기
        if not visited[y]:
            dfs(y)


dfs(v)
print()

# 이제 BFS 수행하기
visited = [False] * (n + 1)  # (중요) 방문 처리 배열
q = deque()  # 큐 만들기
visited[v] = True  # 시작 노드 방문 처리
q.append(v)  # 시작 노드 큐에 넣기
"""
graph[1] = [2, 3, 4]
graph[2] = [1, 4]
graph[3] = [1, 4]
graph[4] = [1, 2, 3]
"""

while q:  # 큐가 빌 때까지 반복
    x = q.popleft()
    print(x, end=" ")
    for y in graph[x]:  # 인접 노드 확인
        if not visited[y]:
            visited[y] = True
            q.append(y)
