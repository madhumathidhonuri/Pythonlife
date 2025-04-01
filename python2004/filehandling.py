#read mode
file=open("madhu.txt",mode="r")
m=file.read() #read() function reads all the data in the txt file
#print(m)
file.close()

file=open("madhu.txt",mode="r")
mm=file.readlines() #converts data in the form of list
#print(mm)
file.close()

file=open("madhu.txt",mode="r")
mmm=file.readline() #reads only one line
#print(mmm)
file.close()

#write mode

file=open("madhu.txt",mode="w")
d=file.write("my mom") #write() writes the data in the text file but previous data will be lost
#print(d)
file.close()

file=open("madhu.txt",mode="a") #if we use append mode data will be not lost
dd=file.write("madhu is daughter of pushpa")
#print(dd)
file.close()


#r+ mode
file=open("madhu.txt",mode="r+")
# print(file.tell()) #tell() function tells about the file pointer location
# print(file.read())
# print(file.tell())
# c=file.read()
# print(c)
# print(file.tell())
# cc=file.write("i am madhumathi reddy")
# print(cc)

# #w+ mode
# file=open("sample.txt",mode="w+") #w+  creates the file
# pass

file=open("madhu.txt",mode="r+")
# print(file.read(5))
# print(file.tell())
# print(file.seek(0))
# file.close()
content=file.read()
print(content)
v=str(content)
print(v)
m=v.split()
print(m)
m.insert(2,"reddy")
print(file.tell())
file.close()
file=open("madhu.txt",mode="w")
print(m)
for i in m:
    print(file.writelines([i]))