
"""
a부터 z까지의 아스키 코드 구하는 방법
print(ord("a")) a = 97
print(ord("b"))
print(ord("c"))
print(ord("d"))
print(ord("e"))
print(ord("f"))
print(ord("g"))
print(ord("z")) z = 122
"""

data = input()

characters = [-1] * 26
# characters[0]: a가 나온 위치
# characters[1]: b가 나온 위치
# ...
# characters[25]: z가 나온 위치

for i in range(len(data)):
    if characters[ord(data[i]) - 97] == -1:
        characters[ord(data[i]) - 97] = i

for x in characters:
    print(x, end=" ")
