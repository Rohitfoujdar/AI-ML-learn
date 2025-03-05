a1=int(input("Enter a Value : "))
a2=int(input("Enter a Value : "))
a3=int(input("Enter a Value : "))
a4=int(input("Enter a Value : "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number of  a1 : ", a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number of  a2 : ", a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number of  a3 : ", a3)
elif(a4>a2 and a4>a3 and a4>a1):
    print("Greatest number of  a4 : ", a4)
else:
    print("error") 