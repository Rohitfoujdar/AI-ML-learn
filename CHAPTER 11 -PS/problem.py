class twoDvactor:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vactor is {self.i}i + {self.j}j")  

class threeDvactor(twoDvactor):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vactor is {self.i}i + {self.j}j + {self.k}k")    


o = twoDvactor(1, 2)
o.show()
e = threeDvactor(1, 2, 3)
e.show()
