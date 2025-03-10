words = ["donkey", "bad", "ganda"]

with open("don.txt") as f:
  content = f.read()
  for word in words:
    content = content.replace(word, "####")

with open("don.txt", "w") as f:
    f.write(content)    