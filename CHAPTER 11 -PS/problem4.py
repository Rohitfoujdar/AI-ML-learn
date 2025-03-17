class Complex:
    def __init__(self, r, i):  #Constructor method
        self.r = r
        self.i = i   #intialize

    def __add__(self, c2):  # Dunder method for addition
        return Complex(self.r + c2.r, self.i + c2.i) 

    def __mul__(self, c2):  # Dunder method for multiplication
        real = self.r * c2.r - self.i * c2.i  
        imag = self.r * c2.i + self.i * c2.r  
        return Complex(real, imag)
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(1, 2)    
c2 = Complex(3, 4)    

print("Addition:", c1 + c2)  
print("Multiplication:", c1 * c2)  
