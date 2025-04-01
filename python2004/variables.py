#in this program madhu is a variable which store the value 21
# madhu=21
# print(madhu)

# mutliple variables storing one value
# for the below program output will be 100
# a=b=c=100
# print(a)

#here is the example to show the tuples example
# for the below program output will be (1,2,3)
# a=1,2,3
# print(a)


#good
#variable names should start with letters or underscores only
# madhu=2004
# _madhu=18
# print(madhu)
# print(_madhu)

#bad
#variable names cannot start with numbers because it produces error
# 1madhu=2
# print(1madhu)

#special characters cannot be used to create a variable @#$%^& because it produces error
# @madhu=218
# print(@madhu)

#special characters cannot be used anywhere because it produces error
# madhu@=14
# print(madhu@)

#variable names are case sensitive
# madhu=18
# Madhu=2
# MADHU=2004
# print(madhu)

#bad
#the below example shows how the variables are case sensitive
# madhu=18
# print(Madhu)


#variable cases
#'''variable cases are of three types 1)camelcase 2)snake_case 3)PascalCase'''
#caamelCase
#madhuMathi=18
#snake_case
#madhu_mathi=2
#PascalCase
#MadhuMathi=2004

#to find address of a variable
# a=10
# print(id(a))

#when two variables have the same value then their address will be same
# a=18
# b=18
# print(id(a))
# print(id(b))

# a=18
# b=-18
# c=18.2
# d=-18.2
# e=True
# f=False
# g=2+3j
# print(type(a),type(b),type(c),type(d),type(e),type(f),type(g))


#type conversions
#coversion of int data type to float datatype
#the below code is the example for implicit conversion(no data loss)
# a=18
# print(float(a))
# coversion of float data type to int data type
# the below code is the example for explicit conversion (data loss)
# a=18.2
# print(int(a))

#program of simple interest
#formula for simple interest is si=(p*t*r)/100
# p=100000
# t=3
# r=1
# si=(p*t*r)/100
# print(si)

#program of compound interest
# p=103000
# r=3
# n=500
# t=4
# ci=p(1+(r/n))^nt
# print(ci)

#input function
# a=int(input("enter the value of a:"))
# b=int(input("enter the value of b:"))
# c=a+b
# print(c)/

#program of (a+b)**2
'''
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
formula=(a+b)**2
print(formula)
'''


