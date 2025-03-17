a=int(input("Enter a number: "))
b=int(input("Enter a number: "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not mean to devide numbers by 0")
else:
    print(f"The division a/b is {a/b}")