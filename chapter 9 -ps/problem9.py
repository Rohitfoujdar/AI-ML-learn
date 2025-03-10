with open("this.txt", "r") as f:
    content_this_txt = f.read()
with open("copy_this.txt", "r") as f:
    content_poem_txt = f.read()
    if (content_poem_txt == content_this_txt):
        print("Yes these files are indential")
    else:
        print("No these files are not indential")
