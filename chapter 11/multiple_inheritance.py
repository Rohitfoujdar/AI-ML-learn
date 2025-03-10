class Employee:
    company = "ITC"
    def show(self, name, sallery):
        print(f"The name of employe is {name} and the sallery is {sallery}")

class Coder:
    language = "Java script"
    def printlanguage(self):
        print(f"Out of all the langauge here is your langauage : {self.language}")
        
class Programmer(Employee, Coder):
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name of employe is {self.name} and he is good with  {self.language} language")

a= Employee()
b= Programmer()

b.show("Rohit" , 1200000)
b.printlanguage()
print(b.company)
