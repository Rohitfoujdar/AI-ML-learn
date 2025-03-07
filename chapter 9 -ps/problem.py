with open("poem.txt") as f:
      content = f.read()
      if("twinkle" in content):
            print(content)
      else:
            print("Do not have content")      