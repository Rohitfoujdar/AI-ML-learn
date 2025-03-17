import streamlit as st

class Vector:
    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)

v1 = Vector([1, 2, 3])
st.write(f"Length of Vector: {len(v1)}")  #Streamlight UI view
