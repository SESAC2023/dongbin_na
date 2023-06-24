"""
arr = [3, 5, 6, 7, 9], n = 5

sum = 3 * (3 + 5 + 6 + 7 + 9)
       += 5 * (3 + 5 + 6 + 7 + 9)
       += 6 * (3 + 5 + 6 + 7 + 9)
       += 7 * (3 + 5 + 6 + 7 + 9)
       += 9 * (3 + 5 + 6 + 7 + 9)

이 함수는 모든 원소에 대하여, 다른 모든 원소를 곱한 것의 합을 구하는 프로그램이다.
결과적으로 2중 반복문이 쓰이기 때문에, 대략 N^2 이라고 하자.

O(N^2)
"""

n = int(input())

print(n ** 2)
print(2)
