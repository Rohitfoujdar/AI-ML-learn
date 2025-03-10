with open("log.txt", "r")as f:
    lines = f.readlines()
    lineno=1
    for line in lines :
        if("python" in line):
            print(f"Yes python is available in line no : {lineno}")
            lineno +=1
            break
        else:
            print("Sorry! Python is not available in this line")
 