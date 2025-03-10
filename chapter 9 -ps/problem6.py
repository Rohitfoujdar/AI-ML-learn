with open("log.txt", "r")as f:
    content = f.read()
    if("python" in content):
        count = content.lower().count("python")
        print(f"Yes python is available in content : {count} time")
    else:
        print("Sorry! Python is not available in content")
 