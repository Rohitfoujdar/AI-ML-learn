Physics=int(input("Enter your physics marks : "))
Chemistry=int(input("Enter your chemistry marks : "))
Math=int(input("Enter your math marks : "))
Biology=int(input("Enter your biology marks : "))
English=int(input("Enter your english marks : "))
Hindi=int(input("Enter your hindi marks : "))

total_p = (100*(Physics + Chemistry + Math + Biology + English + Hindi))/600

if(total_p>=40 and Physics >=33 and Chemistry >=33 and Math >=33 and Biology >=33 and English >=33 and Hindi >=33):
    print("You are paased : ", total_p)

else:
    print("Better luck next time", total_p)    