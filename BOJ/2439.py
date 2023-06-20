"""
j가 i까지 가도록 하기
i = 0일 때, j = [0] => 별의 개수
i = 1일 때, j = [0, 1] => 별의 개수
i = 2일 때, j = [0, 1, 2] => 별의 개수
i = 3일 때, j = [0, 1, 2, 3] => 별의 개수
i = 4일 때, j = [0, 1, 2, 3, 4] => 별의 개수
"""

n = int(input())  # n = 5

for i in range(n):  # i = [0, 1, 2, 3, 4]
    # 앞에서 공백을 출력하고
    for j in range(n - i - 1):
        print(" ", end="")
    # 이어서 별을 출력하고
    for j in range(i + 1):
        print("*", end="")
    print()
