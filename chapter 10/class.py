class Employee:
    language = "py"   #This is class attribute
    salary = 1200000

Rohit = Employee()
Rohit.name= "Rohit foujdar" # This is object attribute / instance attribute
Mayank = Employee()
Mayank.name= "Mayank agrwal"
print(Rohit.name ,Rohit.language, Rohit.salary)
print(Mayank.name, Mayank.salary, Mayank.language)

# Here name is a object attribute and salery and language a class attribute as they directly belong the class