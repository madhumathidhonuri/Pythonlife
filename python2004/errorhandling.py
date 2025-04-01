try:
    print("m")
except:
    print("error occured")
else:
    print("no error")
finally:
    print("excute even if error occured or not")


try:
    print('a'+10)
except Exception as madhu:
    print("error",madhu)


try:
    print('m'+'a'+'d'+'h'+'u')
except:
    print("outer")
else:
    print("no error")
    try:
        print('m'+'a'+'t'+'h'+'i')
    except:
        print("inner")
    else:
        print("no error bro")


#types of errors

print("***indentation error***")
if True:
   print("m")

print('*** type error***')
print(str(1)+'m')

print("***key error***")
d={1:'madhu'}
print(d[1])
print("***indexerror***")
lists=[1,2,3,4,5]
print(lists[0])

print("***keyboard interrupt")
#while True:
    #print("bunny")

print("***syntax error***")
print("...")

print("***FileNotFoundError***")
# file=open("bunny.txt",mode="r")
#m=file.read()
#print(m)

print("***module not found error")
#import madhumadhu

print("***value error***")

# c=int(input())
# print(c)

print("***zero division error")
#print(1/0)

print("***attribute error***")
l=10000
l.append(10)
print(l)