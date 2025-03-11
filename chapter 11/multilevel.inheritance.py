class Employee:
    a=1

class Programmer(Employee):
    b=2

class Manager(Programmer):
    c=3

o = Employee()
o2 = Programmer()
o3 = Manager()
print(o3.a)
print(o3.b)
print(o3.c)

