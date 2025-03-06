'''
factorial(0)=1
factorial(1)=1
factorial(2)=1*2
factorial(3)=1*2*3
factorial(4)=1*2*3*4
factorial(5)=1*2*3*4*5
factorial(n)=n*n-1*..............3*2*1
factorial(n)=n*factorial(n-1)
'''

def factorial(n):
    if(n==1 or n==0):
     return 1
    return n*factorial(n-1)

a = int(input("Enter your number : "))
print(f"factorial number : {factorial(a)}")
