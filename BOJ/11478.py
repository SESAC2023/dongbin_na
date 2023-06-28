"""
목표: 서로 다른 부분 문자열의 개수
  - "부분 문자열"이란, 문자열에서 "연속된 일부분"을 말함

<문제 풀이 아이디어>
- 각 길이마다 모든 가능한 부분 문자열을 확인
예시) 입력: "ababc"
  1) 길이가 1일 때 => a, b, a, b, c      (총 5개)
  2) 길이가 2일 때 => ab, ba, ab, bc   (총 4개)
  3) 길이가 3일 때 => aba, bab, abc   (총 3개)
  4) 길이가 4일 때 => abab, babc      (총 2개)
  5) 길이가 5일 때 => ababc             (총 1개)

전체 길이마다 모든 가능한 부분 문자열을 확인하면,
총 시간 복잡도는? O(N^2)
=> 즉, 그냥 모든 경우의 수를 다 보면 된다.
"""

s = input()  # 입력 문자열
all_sub_strings = set()  # 모든 부분 문자열(집합이므로, 중복 제거)

# 길이를 1부터 N까지 1씩 증가시키며
for length in range(1, len(s) + 1):
    # print("현재 길이:", length)
    # 첫 번째 위치부터 가능한 모든 부분 문자열 확인
    for i in range(0, len(s) - length + 1):
        sub_string = s[i:i + length]
        # print(sub_string)
        all_sub_strings.add(sub_string)

print(len(all_sub_strings))
