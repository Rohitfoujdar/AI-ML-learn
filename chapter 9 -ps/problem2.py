import random

def game():
    print("You ar playing the game...")
    score = random.randint(1, 62)
    #Fetch th high score
    with open("high_score.txt") as f:
        hiscore = f.read()
        if(hiscore != ""):
          hiscore = int(hiscore)
        else:
           hiscore = 0  

    print(f"Your score : {score}")
    with open("high_score.txt", "w") as f:
       if(score>hiscore):
          f.write(str(score))

    return score

game()      