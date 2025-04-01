# python program to check the given number is odd or even
'''
n=int(input("enter the number:"))
print("even number") if n%2==0 else print("odd number")

'''
#python program to check wheather a number is positive or negative
'''
n=int(input("enter the number:"))
if n>0:
    print("positive number")
elif n<0:
    print("negative number")
else:
    print("zero")
'''

#python program to print odd numbers in a range
'''
n=int(input("enter the number:"))
for i in range(1,n,2):
    print(i)
'''

#python program to check given number is palindrome
'''
def palindrome(n):
    return str(n)==reversed(str(n))
n=int(input("enter the number:"))
if palindrome(n):
    print("palindrome number")
else:
    print("its not a palindrome number")
'''
'''
n=int(input("enter the number:"))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if (temp==rev): 
    print("palindrome number")
else:
    print("not a palindrome number")
'''
#python program to reverse a number
'''
n=int(input("enter the number:"))
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("the reverse of a number is :",rev)
'''
'''
slice operator
n=int(input("enter the number:"))
m=int(str(n)[::-1])
print(m)
'''
#python program to print all the numbers that aren't divisible either by 2 or 3
'''
for i in range(0,50):
    if(i%2!=0 and i%3!=0):
        print(i)
'''    
#python program to find the numbers divisuble by 7 and multiples of 5 in a given range
'''
n=int(input())
m=int(input())
for i in range(n,m):
    if (i%7==0 and i%5==0):
        print(i)
'''
    
#python program to print the numbers in a range  divisible by a given number
'''
lower=int(input())
upper=int(input())
n=int(input())
for i in range(lower,upper+1):
    if (i%n==0):
        print(i)
'''

#python program to print tables
"""
for i in range(1,4):
    for j in range(1,11):
        print(i*j)
"""
#python program to print sum of digits of a number
'''
n=int(input("enter the number:"))
total=0
while (n>0):
    dig=n%10
    total=total+dig
    n=n//10
print(total)
'''
#python program to find the sum of digits of a number using recursion
'''
l=[]
def digits(n):
    if n==0:
        return
    dig=n%10
    l.append(dig)
    digits(n//10)
nn=int(input("enter"))
digits(nn)
print(sum(l))
'''
#python program to check armstrong
'''
n=int(input("enter the number:"))
#      153   =      1^3+5^3+3^3      =1+125+27=153
sum=0
temp=n
while (temp>0):
    dig=temp%10
    sum+=dig**3
    temp=temp//10
if n==sum:
    print("armstrong number")
else:
    print("not armstrong number")
'''

#python program to print fibonacci series
'''
n=int(input("enter the range:"))
a=0
b=1
print(a,b,end=" ")
while(n>0):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
'''
'''
l=[1,2,3,4,5,6]
print(l)
n=l[0]**3,l[1]**3,l[2]**3,l[3]**3,l[4]**3,l[5]**3
print(n)
'''
'''
l=[1,2,3,4,5,6]
sum=0
m=[]
for i in l:
    i==l
    n=i**3
    print(n)
    sum=sum+n
print("sum:",sum)
'''

# person eligible for voting
'''
age=int(input("enter the age of the person:"))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")
'''
# to check the number is even or odd
'''
n=int(input("enter the number:"))
if n%2==0:
    print("even")
else:
    print("odd")    
'''
#to check wheather a number is divisible by 7 or not
'''
n=int(input("enter the number:"))
if n%7==0:
    print("divisible")
else:
    print("not divisible")
'''
# multiple of 5
"""
n=int(input("enter the number:"))
if n%5==0:
    print("HELLO")
else:
    print("BYE")   
"""
#electricity bill
'''
unit=int(input("enter the units:"))
price=0
if unit<100:
    price=0
    print(price)
elif unit>=100:
    price=unit*5
    print(price)
elif unit>=200:
    price=unit*10
    print(price)
'''
#to display last digit of a number
'''
n=182004
s=0
while True:
    s=n%10
    print(s)
    break
'''
# last digit is divisible by 3 or not
'''
n=int(input("enter the num:"))
s=n%10
if n%3==0:
    print("yes")
else:
    print("no")
'''
#student grades
'''
marks=int(input("enter the marks:"))
if marks>90:
    print("A")
elif marks>80 and marks<=90:
    print("B")
elif marks>=60 and marks<=80:
    print("c")
else:
    print("D")
'''
#to display tax
'''
cp=int(input("enter the cost price of a bike:"))
tax=0
if cp>100000:
    tax=(15/100)*cp
    print(tax)  
elif cp>50000 and cp<=100000:
    tax=(10/100)*cp
    print(tax)
elif cp<=50000:
    tax=(5/100)*cp
    print(tax)
'''
#leap year 
'''
year=int(input("enter the year:"))
if year%100==0:
    if year%400==0:
        print("leap year")
    else:
        print("no")
if year%4==0:
    print("leap year")
else:
    print("no")
'''
#days
'''
n=int(input("enter the number:"))
if n==1:
    print("monday")
elif n==2:
    print("tuesday")
elif n==3:
    print("wednesday")
elif n==4:
    print("thursday")
elif n==5:
    print("friday")
elif n==6:
    print("saturday")
elif n==7:
    print("sunday")
else:
    print("wrong number")
'''
# Program to check if a number is prime or not
'''
# To take input from the user
num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
'''
# vowel
'''
c=input("enter the character:")
v=['a','e','i','o','u']
if c in v:
    print("yes")
else:
    print("no")
'''
#attendance
'''
w=int(input("enter the working days:"))
a=int(input("enter the no of days absent:"))
p=(w-a/w)*100
print(p)
if p>=75:
    print("can sit")
else:
    print("not allowed")
'''
#bonus
'''
s=int(input("enter the salary:"))
t=int(input("enter the years:"))
bonus=0
if t>10:
    bonus=(10/100)*s
    print(bonus)
elif t>=6 and t<=8:
    bonus=(8/100)*s
    print(bonus)
elif t>6:
    bonus=(5/100)*s
    print(bonus)
'''
'''
m=[]
for i in range(5):
    n=input("enter the colors:")
    m.append(n)
print(m)
'''
#numbers 
"""
m=[]
for i in range(10):
    n=int(input("enter numbers:"))
    if n%2==0:
        m.append(n)
print(m)
"""
#to find largest number in the list without using inbuilt function
'''
A=[23,12,45,67,55]
A.sort()
print(A[-1])
'''
'''
n=()
i=0
while(i<5):
    F1=input("enter the fruit name:")
    n=n+(F1,)
    i=i+1
print(n)
'''
'''
file=open("madhu.txt",mode="r")
c=file.readlines()
print(c)
file.close()    
'''
#table
'''
n=int(input("enter:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)
'''
'''
n=int(input("enter the number of series:"))
a=0
b=1
c=a+b
print(a,b,end=" ")
while(n>=0):
    a=b
    b=c
    c=a+b
    print(c,end=" ")
    n=n-1
'''