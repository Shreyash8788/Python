lst = [1,2,3,4,3,1,]

duplicates = []

for item in lst:
    if lst.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print(duplicates)