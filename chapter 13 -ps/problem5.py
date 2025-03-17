from functools import reduce
l = [1, 24, 55, 88, 77, 89, 99, 174, 53, 286, 350, 259, 466]
def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))


