lst = [1,2,3,4,5]
target = 7

length = len(lst)

result = []

for i in range(length):
    for j in range(i+1,length):
        if lst[i]+lst[j]==target:
            result.append((lst[i],lst[j]))

print(result)
