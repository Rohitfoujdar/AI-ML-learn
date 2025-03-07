import random
'''
snake = 1
water = -1
gun = 0
'''

computer = random.choice([1, -1, 0])
youstr= input("Enter your choice : ")
youdic= {"s": 1, "w":-1, "g":0}
retrevestrg={1:"snake", -1:"water", 0:"gun"}
you=youdic[youstr]

print(f"Your choice {retrevestrg[you]}\nComputer choice {retrevestrg[computer]}")

if(computer == you):
    print("Draw")
else:
     if((computer - you)== -2 or (computer-you)==1):
            print("You win")
   