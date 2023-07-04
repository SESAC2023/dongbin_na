import sys

sys.setrecursionlimit(int(1e6))

n = int(input())  # 사람의 수
arr = []
for i in range(n):
    line = list(map(int, input().split()))
    arr.append(line)
m = n // 2
visited = [False] * n  # 각 원소가 선택되었는가
selected = set()

# cnt = 0

min_value = 1e10


# depth: 현재 재귀에서 선택된 원소의 개수
def dfs(depth, now):
    global min_value
    if depth == m:
        # 실제로 현재 경우에 대하여 처리하는 부분
        a_team = []
        b_team = []
        for i in range(n):
            if i in selected:  # A 팀
                a_team.append(i)
            else:  # B 팀
                b_team.append(i)
        # print(a_team, b_team)
        a_total = 0
        for i in range(m):
            one = a_team[i]
            for j in range(i, m):
                two = a_team[j]
                a_total += arr[one][two]
                a_total += arr[two][one]
        b_total = 0
        for i in range(m):
            one = b_team[i]
            for j in range(i, m):
                two = b_team[j]
                b_total += arr[one][two]
                b_total += arr[two][one]
        dif = abs(a_total - b_total)
        min_value = min(min_value, dif)
        # cnt += 1
        return
    for i in range(now, n):
        if visited[i]:
            continue
        # 백트래킹은 3단계로 재귀 호출
        # (1) 원소 넣기
        visited[i] = True
        selected.add(i)
        dfs(depth + 1, i)  # (2) 재귀 호출
        # (3) 원소 빼기
        visited[i] = False
        selected.remove(i)


dfs(0, 0)
# print(cnt)
print(min_value)
