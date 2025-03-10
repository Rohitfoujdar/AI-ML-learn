class Employee:
    language = "py"   
    salary = 1200000

    def getinfo(self):  #self a normal name
        print(f"The language is {self.language} and the sallery is {self.salary}")

    def greet(self):
        print("Good morning")    

Rohit = Employee()
Rohit.language= "java" 
Rohit.getinfo()
Rohit.greet()
# Employee.getinfo(Rohit)
