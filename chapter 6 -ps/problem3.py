p1= "Make a lot of money"
p2= "Subscribe"
p3= "Click Now"
p4= "Win real cash"

message = input("Enter your message : ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)) :
    print("This comment is spam")