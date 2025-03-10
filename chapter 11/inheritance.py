class Employee:
    company = "ITC"
    def show(self, name, sallery):
        print(f"The name of employe is {name} and the sallery is {sallery}")


# class Programmer:
#     company = "ITC infotech"
#     def show(self):
#         print(f"The name of employe is {self.name} and the sallery is {self.sallery}")
#     def showlanguage(self):
#         print(f"The name of employe is {self.name} and he is good with  {self.language} language")
        
class Programmer(Employee): #This is inheritante class 
    company = "ITC infotech"
    def showlanguage(self):
        print(f"The name of employe is {self.name} and he is good with  {self.language} language")

a= Employee()
b= Programmer()

b.show("Rohit" , 1200000)
print(b.company)
