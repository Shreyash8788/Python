lst  = [1,2,3,4,5]
largest = lst[0]

for item in lst:
    if item > largest:
        largest = item

print(largest)