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
    for j in range(i + 1):
        print("*", end="")
    print()
