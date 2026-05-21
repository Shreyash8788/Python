lst = [3,5,3,2,4,1]

n = len(lst)

for i in range(n):
    for j in range(0,n-i-1):
         if lst[j] > lst[j+1]:  #if you want list sort in dessending order then change the condition to "<"
            lst[j],lst[j+1] = lst[j+1],lst[j]

print(lst)