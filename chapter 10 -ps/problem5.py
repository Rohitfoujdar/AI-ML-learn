from random import randint

class train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"Ticket is booked in train No.{self.trainNo} from {fro} to {to}")
    def  getstatus(self):
        print(f"Train No. {self.trainNo} running on time")
    def getfare(self, fro, to):
        print(f"Ticket fare in train no. {self.trainNo} from {fro} to {to} is {randint(1, 555)}")
        
trainNo = int(input("Enter your train number : "))
fro = input("From : ")
to = input("To : ")

a = train(trainNo)
a.book(fro, to)
# a.getstatus()
# a.getfare(fro, to)


