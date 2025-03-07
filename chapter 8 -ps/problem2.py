# f = int(input("Enter your number : "))
# c= 5*(f-32)/9

# print(c)

def f_to_c(f):
    c= 5*(f-32)/9
    return c

f = int(input("Enter temprature in F : "))
c=(f_to_c(f))
print(f"{round(c, 2)}°C") #round use for desimal number problem