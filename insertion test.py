import random
y = 1000000
items = [random.randint(0,10) for x in range(y)]
len_items = len(items)

for index in range(1,len_items):
    current = items[index]
    index2 = index

    while index2 > 0 and items[index2 - 1] > current:
        items[index2] = items[index2 -1]
        index2 = index2-1

    items[index2] = current
print(items)
