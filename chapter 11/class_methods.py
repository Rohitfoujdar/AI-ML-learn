class Employee:
    a=1
    @classmethod  #Directly use class methods
    def  show(cls):
        print(f"The class attribute is {cls.a}")

o = Employee()
o.a = 45
o.show()
