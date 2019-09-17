list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for value1 in list1:
    for value2 in list2:
        list3.append(value1 * value2)

print(list3)
