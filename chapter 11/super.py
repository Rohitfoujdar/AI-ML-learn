class Employee:
    def __init__(self):
       print("Employee constructor")
    a=1   

class Programmer(Employee):
    def __init__(self):
       super().__init__()
       print("Programmer constructor")
    b=2

class Manager(Programmer):
    def __init__(self):
       super().__init__()   #Super constructor allow the parent constructor
       print("Manager constructor")
    c=3

o = Manager()
print(o.a, o.b, o.c)

