#single parameter function
def madhu(m):                   #function defination
    print("madhumathi",m)
madhu(18)                       #function call


def madhumathi(a,b):            #function defination
    print("i am madhuu",a,b)
madhumathi(2004,18)             #function call

#multiple parameter function
def manisha(a,b,c):             #function defination
    print("i am manisha",a,b,c)
manisha(2,18,2004)              #function call



def dhonuri(name):
    print("i am madhu",name)
n=input("enter the name:")
dhonuri(n)


#arbitary parameter "when you want to assign more arguments to single one" *
def name(*n):
    print("hi",n)
name(1,2,2,32,5,67,4,5)

# keyword arguments these store the data in the dictionary format **
def namee(**n):
    print("hi",n)
namee(n="madhu",age=21)


#nested function
def outer_function():
    print("hi,hello! good morning")
    def inner_function():
        print("hiii")
    inner_function()
outer_function()


#mutiple functions in import cheyadam
'''
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
'''

# lambda function

f=lambda a,b,c:a+b+c
print(f(1,7,3))

l1=[1,2,3,4,5,6]
l2=[]
for i in l1:
    t=lambda a:a+1
    l2.append(t(i))
print(l2)

#filter function

l=[1,2,32,44,55,6]
def fun(m):
    if m<18:
        return False
    else:
        return True
adults=filter(fun,l)
print(list(adults))



#map function

def calculateAddition(n):
    return n+n
num=[1,2,3,4,5,6]
f=map(calculateAddition,num)
print(list(f))


from functools import reduce

d=reduce(lambda a,b:a+b,[2,3,4,5])
print(d)


#yeild keyword
#yield keyword controls the generator function

def madhumathii():
    yield 2
    yield 18
    yield 2004
m=madhumathii()
print(m.__next__())
print(m.__next__())
print(m.__next__())


