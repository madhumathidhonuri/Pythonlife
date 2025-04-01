#python program to print hello world
print("Hello World!")

#python program to add two numbers
'''
a=int(input("enter the value:"))
b=int(input("enter the value:"))
c=a+b
print("the sum of {0} and {1} is {2}".format(a,b,c))
'''
#python program to find the squareroot of a number
'''
a=int(input("enter the value:"))
square=a**0.5
print("the square of {0} is".format(a),square)
'''
#python program to calculate the area of a triangle
'''
a=float(input("enter the value:"))
b=float(input("enter the value:"))
c=float(input("enter the value:"))
s=(a+b+c)/2 #semiperimeter of a triangle
print(s)
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(area)
'''
#python program to solve quadratic equation

#quadratic eqn=ax**2+bx+c
'''
a=float(input("enter the value:"))
b=float(input("enter the value:"))
c=float(input("enter the value:"))
d=b**2-(4*a*c)#determinant
print(d)
sol1=-b-((b**2-(4*a*c))/(2*a))
sol2=-b+((b**2-(4*a*c))/(2*a))
print("the solutions of quadratic equations is {0},{1}".format(sol1,sol2))
'''
#python progarm to swap two variables
'''
a=5
b=10
temp=a
a=b
b=temp
print("the value of a after swapping is {}".format(a))
print("the value of b after swapping is {}".format(b))
'''
#python program to generate a random number
'''
import random #random module
print(random.randint(0,25))
'''
#python program to convert kilometers into miles
'''
1 kilometer=1000meters
1 mile=1.609344 kilometers

km=float(input("enter kilometers:"))
con_fac=0.62137119
miles=km*con_fac
print("{} kilometers equal to {} miles".format(km,miles))
'''
#python program to convert celsius to fahrenheit
'''
1 celsius=33.8 fahrenheit

c=float(input("enter celsius:"))
celsius=33.8
fahrenheit=(c*1.8)+32
print("{} celsius is equal to {} fahrenheit".format(c,fahrenheit))
'''
#python program to check the number is positive,negative or 0
'''
n=int(input("enter the number:"))
if n>0:
    print("{} is positive".format(n))
elif n<0:
    print("{} is negative".format(n))
else:
    print("{} is 0".format(n))
'''
#python program to check if a number is odd or even
'''
n=int(input("enter the number:"))
if n%2==0:
    print("{} is even number".format(n))
else:
    print("{} is odd number".format(n))
'''
#python program to check leap year
'''
y=int(input("enter the year:"))
if y%100==0 and y%400==0:
    print("{} is a leap year".format(y))
else:
    print("{} is not a leap year".format(y))
'''
#python program to find the largest among three numbers
'''
n1=int(input("enter the n1:"))
n2=int(input("enter the n2:"))
n3=int(input("enter the n3:"))
if n1>=n2 and n1>=n3:
    largest=n1
    print("the largest number is:",largest)
elif n2>=n1 and n2>=n3:
    largest=n2
    print("the largest number is",largest)
    
else:
    print("n3 is largest")

l=[1,7,2,3,168,21]
print(max(l))
'''
#python progarm to check prime number
'''
n=int(input("enter the number:"))
if n%2!=0:
    print("{} is prime number".format(n))
else:
    print("{} is not a prime number".format(n))
'''