##################################################
#               File Handling
##################################################
# READ MODE

# READ TOTAL FILE
data = open("demo.txt",mode="r")
print(data.read())
data.close()
print()

# READ FIRST LINE ONLY
data = open("demo.txt",mode="r")
print(data.readline())
data.close()
print()

# READ ALL LINES
data = open("demo.txt",mode="r")
print(data.readlines())
data.close()
print()

# READ ONLY SOME STRINGS USING INDEX
data = open("demo.txt",mode="r")
print(data.read(10))
print()

##################################################
# WRITE MODE

data = open("demo.txt",mode="w")
data.write("hello every one...")
data.close()
print()

##################################################
# APPEND MODE

data = open("demo.txt",mode="a")
data.write("PYHON LIFE")
data.close()
print()

##################################################
# TELL MODE AND SEEK MODE

data = open("demo.txt",mode="r")
print(data.tell())
print(data.read())
print(data.tell())
print(data.seek(5))
print(data.tell())
data.close()
print()

##################################################
# r+ MODE

with open("demo.txt","r+") as d: #r+ mode /read and write
    print(d.tell()) #cursor position
    print(d.read()) # read total file
    print(d.tell()) # after read cursor position
    d.seek(0)
    d.write("hello..") # hello.. replace the text in this r+ mode
    print(d.read())
    d.close()

##################################################
# w+ MODE

with open("demo.txt","w+") as f:
    print(f.read()) # earse all the data when using read in w+ mode
    f.write("python programming language")
    print(f.tell())
    f.seek(0)
    f.write("srikanth") # hello.. replace the text in this r+ mode
