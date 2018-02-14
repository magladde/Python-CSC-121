list1 =[[x,y] for x in range(7) if x % 2 == 1
              for y in range(4) if y % 2 == 0]
print(list1)

list1 = []
for x in range(7):
    if x % 2 == 1:
        for y in range(4):
            if y % 2 == 0:
                list1.append([x,y])
print(list1)
