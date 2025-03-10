class Programmer :
    company = "Microsoft"
    def __init__(self, name, salary, pin):
       self.name = name
       self.salary = salary
       self.pin = pin

name = input("Enter your name : ")
salary = int(input("Enter your saller : "))
pin = int(input("Enter your pincode : "))

p= Programmer(name, salary, pin)
print(p.name, p.salary, p.pin, p.company)