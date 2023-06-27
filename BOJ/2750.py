import sys
import math
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n = int(input())

arr = []
for i in range(n):
    x = int(input())
    arr.append(x)

arr.sort() # 기본적으로 오름차순 정렬 수행

for x in arr:
    print(x)
