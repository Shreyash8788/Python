import copy

original = [[1,2],[3,4]]
shallow = copy.copy(original)

shallow[0][1] = 10

print(original)
# shallow copy create a new object but when we change in shallow copy the original list will be change

fixed = [[1,2],[3,4]]
deepcopy = copy.deepcopy(fixed)

deepcopy[1][0] = 10

print(fixed)
# Deep copy also create new object but when we change copyed list it does't effect on original list.
