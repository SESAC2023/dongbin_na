import sys
input = sys.stdin.readline

test_case = int(input())

for tc in range(test_case):
    a, b = map(int, input().split())
    print(f"Case #{tc + 1}: {a + b}")
