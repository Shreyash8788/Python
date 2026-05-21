def flatten_list(nested_lst):
    flat = []
    for sublist in nested_lst:
        for item in sublist:
            flat.append(item)
    print(flat)

lst = [[1,2],[3,4],[5,6]]
flatten_list(lst)




flatten = [item for sublist in lst for item in sublist]
print(flatten)