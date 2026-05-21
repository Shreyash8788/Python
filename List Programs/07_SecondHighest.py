def find_second_high(lst):
    if len(lst) < 2:
        return False
    
    largest = second = float("-inf") #to very small values (-inf).

    for num in lst:
        if num > second:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float("-inf") else None

lst = [43,123,6,3,1]
print(find_second_high(lst))
       