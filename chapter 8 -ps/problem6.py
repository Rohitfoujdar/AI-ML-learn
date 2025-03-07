def inch_to_cms(n):
    if(n==0):
        return 
    a= n*2.54
    return a

n= int(input("Enter your number : "))
print(f"{inch_to_cms(n)}cm")