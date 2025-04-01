import math
d='''
1.addition
2.subtraction
3.multiplication
4.division
5.modulous
6.square
7.cube
8.factorial
9.leap year
10.trignometry
'''
print(d)
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def mod(a,b):
    print(a%b)
def square(a):
    print(a*a)
def cube(a):
    print(a*a*a)
n=int(input("enter the number:"))
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
year=int(input("enter the year:"))
def leapyear(year):
    return((year%4 ==0) and (year%100!=0) or (year%400==0))
if leapyear(year):
    print("{} is a leapyear".format(year))
else:
    print("{} is not a leapyear".format(year))
def trig():
    print(math.cos(n))
    print(math.sin(n))
    print(math.tan(n))

if True:
    pass
    while True:
        option=int(input("enter the option:"))
        if option==1:
           add(a,b)
        elif option==2:
           sub(a,b)
        elif option==3:
           mul(a,b)
        elif option==4:
           div(a,b)
        elif option==5:
           mod(a,b)
        elif option==6:
           square(a)
        elif option==7:
           cube(a)
        elif option==8:
            factorial(n)
        elif option==9:
            leapyear(year)
        elif option==10:
            trig()
        else:
           print("incorrect option")
           break
else:
    print("invalid")