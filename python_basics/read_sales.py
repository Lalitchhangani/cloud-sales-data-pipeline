print("Hello Lalit")

file = open("data/sales.csv", "r")

data = file.read()

print(data)

file.close()