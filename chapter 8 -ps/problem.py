
# def number():
#     a=int(input("Enter your number : "))
#     b=int(input("Enter your number : "))
#     c=int(input("Enter your number : "))

#     if (a>b and a>c):
#         print("Greatest number of : ", a)
#     if (b>a and b>c):
#         print("Greatest number of : ", b)
#     if (c>b and c>a):
#         print("Greatest number of : ", c)

# number()   


def number():
    a=int(input("Enter your number : "))
    b=int(input("Enter your number : "))
    c=int(input("Enter your number : "))

    if (a>b and a>c):
       return a
    elif (b>a and b>c):
       return b
    elif (c>b and c>a):
       return c
    else:
       print("Sorry!")

print(f"Greatest number of : {number()}")