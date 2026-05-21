import sys

lst = []
print(sys.getsizeof(lst))
# By default size of list is 56

lst.append(1)
print(sys.getsizeof(lst))

lst.append(2)
print(sys.getsizeof(lst))
# This shows how Python allocates extra memory in advance to optimize performance.