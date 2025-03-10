import random

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)

    # Fetch the high score
    try:
        with open("high_score.txt", "r") as f:
            hiscore = f.read().strip()
            hiscore = int(hiscore) if hiscore else 0  # Convert to int if not empty
    except FileNotFoundError:
        hiscore = 0  # Set high score to 0 if file does not exist

    print(f"Your score: {score}")

    # Update high score if the current score is greater
    if score > hiscore:
        with open("high_score.txt", "w") as f:
            f.write(str(score))
        print("New high score!")

    return score

game()
