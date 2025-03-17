b = 89  #Global variable
def fun():
    global b # The change of global variable 
    b =3  #Local Variable
    print(b)

fun()
print(b)