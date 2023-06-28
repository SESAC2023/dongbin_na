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


""" Solution 2

데이터의 개수 N: 최대 50만
쿼리의 개수 M: 최대 50만

1) 데이터 입력 후에 정렬: O(NlogN) => 시간 초과 X
2) 각 쿼리마다 이진 탐색 수행: O(MlogN) => 시간 초과 X

즉, 최종 시간 복잡도: O(NlogN + MlogN)
"""
"""
from bisect import bisect_left, bisect_right


# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


n = int(input())  # 데이터의 개수 N
# 전체 데이터 입력받기
arr = list(map(int, input().split()))

m = int(input())  # 쿼리의 수 M
# 개수를 세고자하는 쿼리 데이터들
queries = list(map(int, input().split()))

# 이진 탐색을 위해 데이터 정렬이 필요
arr.sort()  # O(NlogN)

# 각 쿼리마다 이진 탐색 수행: O(MlogN)
for query in queries:
    cnt = count_by_range(arr, query, query)
    print(cnt, end=" ")
"""
