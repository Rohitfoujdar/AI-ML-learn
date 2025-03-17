#Map 
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square = lambda x: x*x
sqrmap = map(square, l)
print(list(sqrmap))

#filter
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
print(list(onlyEven))

from functools import reduce  # Import reduce from functools

# Define the list to be reduced
l = [1, 2, 3, 4, 5]

# Sum function
def sum(a, b):
    return a + b

# Multiplication function (lambda)
multi = lambda x, y: x * y  # Corrected lambda to take two arguments

# Use reduce to apply the functions
print("Sum of list:", reduce(sum, l))
print("Product of list:", reduce(multi, l))