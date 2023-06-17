data = input() # data = "1 2"
data = data.split(" ") # data = ["1", "2"]
data = list(map(int, data)) # data = [1, 2]

a = data[0]
b = data[1]

print(a / b)
