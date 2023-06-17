a = int(input())
b = int(input())

x_1 = b % 10
x_2 = (b // 10) % 10
x_3 = (b // 100) % 10

print(a * x_1)
print(a * x_2)
print(a * x_3)
print(a * b)
