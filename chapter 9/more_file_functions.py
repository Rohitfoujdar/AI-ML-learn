f = open("file.txt")
# lines = f.readlines()
# print(lines)

# lines1 = f.readline()
# print(lines1)
# lines2 = f.readline()
# print(lines2)
# lines3 = f.readline()
# print(lines3)
# lines4 = f.readline()
# print(lines4)

line= f.readline()
while(line != ""):
    print(line)
    line= f.readline()

f.close()