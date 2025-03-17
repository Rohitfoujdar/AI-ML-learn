import streamlit as st

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x , self.y + other.y , self.z + other.z )    
        return result
    
    def __mul__(self, other):  # Dunder method for multiplication
        result = self.x * other.x + self.y *other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

st.write(v1 + v2)
st.write(v1 * v2)

st.write(v1 + v3)
st.write(v1 * v3)
