# madhu=18
# print(madhu)
# print(type(madhu)) # to know the data is of which type
# print(id(madhu)) #to find the address
'''
n=2
print("prime") if n%2==0 else print("not prime") #short hand if else

if 2<18: print("yes") #short hand if


for i in 'madhumathi':
    if i=='u':
        break # breaks the execution
    print(i)


for i in 'madhumathi':
    if i=='a':
        continue #skips
    print(i)
        
for i in 'madhumathi':
    if i=="x":
        pass # it will not produce error
    print(i)
'''   
# for i in range(0,11):
#     for j in range(0,11):
#         print(i*j,end=" ")
#     print()
    
# lists
'''
a=[1,'madhu',2.2,'a',22.456]
print(type(a))
print(id(a))
print(a) 
print(a.count(2.2))
print(len(a))
a.append(18) # adds at last
print(a)
a.extend([26,2,2003])#adds multiple elements
print(a)
c=a.copy()#copies the list into another variable
print(c)
c.reverse() # reverse the list
print(c)
c.insert(4,12) # insert(location,element)
print(c)
print(c.index(22.456))
b=[3,625,23,64,856]
b.sort()# ascending order
print(b)
b.sort(reverse=True)#descending order
print(b)
b.pop(4)
print(b)
b.remove(856)
print(b)
b.clear() # empty the list
print(b)
'''

#strings
'''
a="madhu is a awesome girl with innocent face"
print(a.upper())# capital letters
print(a.lower())# small letters
print(a.count('a')) # counts how many times repeated
print(a.index('face')) # position
print(a.find('innocent'))
print(a.startswith('with')) #true or false
print(a.endswith('face'))
print(a.isalpha())
print(a.isalnum())
print(a.isnumeric())
print(a.title())
print(a.lstrip())
print(a.rstrip())
print(a.split())
c="$".join(a)
print(c)
'''
#dictionary
'''
a={'name':'madhu','age':21,'sex':'female','DOB':'18-02-2004'}
print(type(a))
print(id(a))
print(a)
print(a.get('DOB'))
print(a.keys())
print(a.values())
print(a.items())
print(a.pop('sex'))
print(a)
b=a.update({'name':'madhumathi'})
b=a.copy()
print(b)
a={1:561}
b=a.clear()
print(b)
'''
#tuples
'''
a=(1,2,3)
b=(4,5,6)
# print(type(a))
# print(id(a))
print(list(b))
print(tuple(zip(a,b)))
print(len(a)) #how many elements
print(min(a)) #smallest number
print(max(a)) #largest number
print(sum(a)) #adds
n=[] #concatenation
for i,j in zip(a,b):
    c=i+j
    n.append(c)
print(tuple(n))
#membership
print(1 in a)
print(4 in a)
print(4 not in a)
#identity
print(a is b)
print(a is not b)
'''
#sets
'''
a={1,5,3,9,2}
print(a)
print(a.add(11))
print(a)
b=a.copy()
print(b)
print(b.pop())
print(b.update(['madhu',45,56,24]))
print(b)
print(b.remove('madhu'))
print(b)
print(b.clear())
print(b)
s1={1,2,3,45,1,2,8,7}
s2={8,9,7,6,5,4,3,6,5}
print(s1)
print(s2)
a=s1.union(s2)
print(a)
print(s2.union(s1))
print(s1.intersection(s2))
print(s2.intersection(s1))
print(s1.difference(s2))
print(s2.difference(s1))
print(s1.symmetric_difference(s2))
print(s2.symmetric_difference(s1))
'''
#functions
# def madhu(a):
#     print("i am madhumathi",a)
# a=int(input("enter the value:"))
# madhu(a)

# def madhuu(a,b):
#     print("he is a boy",a,b)
# a=int(input("enter the value:"))
# b=int(input("enter the value:"))
# madhuu(a,b)

# def madhuuu(a,b,c):
#     print("she is a girl",a,b,c)
# a=int(input("enter the value:"))
# b=int(input("enter the value:"))
# c=int(input("enter the value:"))
# madhuuu(a,b,c)

# def manisha(*n):
#     print("they are learning a course",n)
# manisha('python','java','c','c++','devops')

# def madhumathi(**n):
#     print("this is a keyword argument",n)
# madhumathi(n="smile",age=21)

# def cat(a):
#     print("this animal belongs to tiger family",a)
#     def dog(a):
#         print("this animal belongs to dog family",a)
#     dog("dog")
# cat("named cat")

# f=lambda a,b,c:a*b+c
# print(f(1,2,3))

# l1=[2,4,6,8]
# l2=[]
# for i in l1:
#     t=lambda a:a+1
#     l2.append(t(i))
# print(l2)

# n=[1,2,3,4,5,6,7,8,9,10]
# def fun(n):
#     if n%2==0:
#        return True
#     else:
#        return False
# num=map(fun,n)
# print(list(num))
# 

def swapList():
    l1=[1,2,3,4,5]
    l2=[6,7,8,9,10]
    def swap():
        l1=l2
        print("after swapping l1 is:",l1)
    swap()
    def swaps():
        l2=l1
        print("after swapping l2 is:",l2)
    swaps()
swapList()