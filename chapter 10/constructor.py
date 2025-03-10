class Employee:
    language = "py"   
    salary = 1200000

    def __init__(self, name , language, salary):
         self.name=name
         self.language=language
         self.salary=salary
         print("This is duder function in python") #This is dunder method in pythod its automatically called function

    def getinfo(self):  #self a normal name
        print(f"The language is {self.language} and the sallery is {self.salary}")
    
    def greet():
        print("Good morning")    

Rohit = Employee("Harry", "js", 1300000)
print(Rohit.name, Rohit.salary, Rohit.language)