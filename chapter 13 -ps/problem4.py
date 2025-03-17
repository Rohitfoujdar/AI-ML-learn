def divi5(n):
    if(n%5 == 0):
        return True
    return False

a = [1, 5, 36, 25, 90, 77, 55]
print(list(filter(divi5, a)))