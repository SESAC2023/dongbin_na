x = int(input())
y = int(input())

if x > 0:  # 1사분면 혹은 4사분면
    if y > 0:
        print(1)
    else:
        print(4)
else:  # 2사분면 혹은 3사분면
    if y > 0:
        print(2)
    else:
        print(3)
