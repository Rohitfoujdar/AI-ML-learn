with open("don.txt") as f:
    content = f.read()

    replace = content.replace("donkey", "####")

with open("don.txt", "w") as f:
    f.write(replace)    