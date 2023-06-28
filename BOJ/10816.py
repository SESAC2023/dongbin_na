"""
<문제 요구사항>
숫자 카드 N개가 있다.
쿼리 M개가 주어진다.
=> 이때, 쿼리에 해당하는 데이터의 개수를 찾는 문제
* 유사 문제: 계수 정렬, 카운터(counter)

데이터의 개수가 500,000개이므로,
단순히 counter를 이용해서 해결 가능
=> counter를 사용하면 특정 데이터의 개수에 접근하기 위해 O(1) 필요
따라서 전체 시간 복잡도는 O(N + M)
"""

n = int(input())  # 데이터의 개수
arr = list(map(int, input().split()))  # 전체 데이터 입력

# 우리가 해야 할 일은? 목표: 각 데이터가 "등장한 횟수"를 구하는 것

counter = dict() # 사전 자료형은 데이터 접근을 위해 O(1)만큼
for x in arr:
    if x not in counter: # 처음 보는 데이터인 경우
        counter[x] = 1 # 1번 등장했으므로, 카운트는 1
    else:
        counter[x] += 1 # 등장 횟수를 1만큼 증가

m = int(input()) # 쿼리의 수
queries = list(map(int, input().split())) # 쿼리 데이터 입력

for query in queries:
    if query in counter: # 한 번 이상 등장했다면
        print(counter[query], end=" ")
    else: # 한 번도 등장하지 않았다면
        print(0, end=" ")
