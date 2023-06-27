#토마토

# 시간 초과!!!!!!!!!!!!!!!!!!!!!!!ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
import sys
from collections import deque

sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline
col, row = map(int, input().split())

# 4가지 방향에 대한 정의: 상, 하, 좌, 우
dx = [-1, 1, 0, 0]  # 행 방향
dy = [0, 0, -1, 1]  # 열 방향

# 그래프 입력
graph = [list(map(int, input().split())) for _ in range(row)]
# 방문 처리 배열: 거리 값(distance)을 기록
# -1인 경우: 방문한 적이 없는 위치, 그렇지 않은 경우, 최단 거리 값을 가지고 있음
visited = [[-1] * col for _ in range(row)]

q = deque()  # 탐색 시작 토마토 좌표(원소가 1인 좌표)를 모두 큐에 넣기
for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:  # 익은 토마토가 있는 경우
            q.append((i, j))  # 큐에 삽입
            # 시작 위치(처음 토마토가 있는 위치)까지의 최단 거리는 0
            visited[i][j] = 0

while q:  # 큐가 빌 때까지 반복
    x, y = q.popleft()  # 익은 토마토 (x, y)의 위치를 구하기
    # 현재 위치에서 인접한 4가지 공간을 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 공간을 벗어난다면 무시
        if nx < 0 or nx >= row or ny < 0 or ny >= col:
            continue
        # 벽이라면 무시
        if graph[nx][ny] == -1:
            continue
        # 안 익은 토마토가 있다면, 익도록 처리
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            # 최단 거리 구할 때는 이전 위치까지의 최단 거리 + 1
            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))

possible = True
answer = 0  # 최댓값 계산
for i in range(row):
    for j in range(col):
        # 도착 불가능하면서, 벽이 아닌 경우
        if visited[i][j] == -1 and graph[i][j] != -1:
            possible = False  # 모든 위치를 익게 만드는 것이 불가능
        answer = max(answer, visited[i][j])  # answer에는 최댓값이 담김

if possible:
    print(answer)
else:
    print(-1)
