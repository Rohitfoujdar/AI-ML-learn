class Demo:
    a = 4

o= Demo()
print(o.a) # Print the class attribute because instant attribute is not present
o.a = 2 #This is instant attribute
print(o.a) # Print the instant attribute because instant attribute is available
print(Demo.a) #This is class attribute