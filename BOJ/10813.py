n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

for q in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    arr[x], arr[y] = arr[y], arr[x]
    
    """ 아래랑 같은 기능임
    temp = (b, a)
    a = temp[0]
    b = temp[1]
    """

for x in arr:
    print(x, end=" ")
