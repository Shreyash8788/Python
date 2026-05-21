# Practice
lst = [1,2,4,5,3]
target = 7
result = []
n = len(lst)
for i in range(n):
    for j in range(i+1,n):
        if lst[i]+lst[j]==target:
            result.append((lst[i],lst[j]))

print(result)

