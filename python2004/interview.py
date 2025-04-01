#python program to check number is positive,negative or neutral
n=int(input("enter the number:"))
if n>0:
    print("{} is positive".format(n))
elif n<0:
    print("{} is negative".format(n))
else:
    print("{} is neutral".format(n))
    

#python program to check whether the number is odd or even
    
num=int(input("enter the number:"))
print("EVEN number") if num%2==0 else print("ODD number")


#python program to check the year is a leap year

#year is divisible 4 but not 100
#year is divisible by 4 and 400

year=int(input("enter the year:"))
def checkyear(year):
    return (((year%4==0) and (year%100!=0) or (year%400==0)))
if checkyear(year):
    print("{} is leap year".format(year))
else:
    print("{} is not a leap year".format(year))
    


#python program to find the largest number among the three input number
    
num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
num3=int(input("enter the num3:"))
if num1>num2 and num1>num3:
    print("{} is greater".format(num1))
elif num2>num1 and num2>num3:
    print("{} is greater".format(num2))
else:
    print("{} is greater".format(num3))


#using max function
l=[2,18,2004,26,2003,4,28]
print(max(l))