# prints returned iterator info
x = [1, 2, 3]
y = [4, 5, 6]
z_list = zip(x + y)
print(z_list)

# prints zipped lists
x = [1, 2, 3]
y = [4, 5, 6]
z_list = list(zip(x, y))
print(z_list)

# prints unzipped lists
x2, y2 = zip(*z_list)
print(list(x2))
print(list(y2))
