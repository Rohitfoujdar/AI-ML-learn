f = open ("file.txt") 
data= f.read() 
print(data)
f.close

#The same can be written using with statement like this:
with open("file.txt") as f:
    print(f.read())

#You dont have to explictily close the file
