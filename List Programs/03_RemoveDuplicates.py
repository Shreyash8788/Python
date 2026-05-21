def removeDuplicate(lst):
    result = []

    for item in lst:
        if item not in result:
            result.append(item)
    return result
    
lst = [1,2,3,2,4,2,5]
print(removeDuplicate(lst))
