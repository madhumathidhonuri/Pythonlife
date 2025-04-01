'''
list is used to store mutlite data types
list is mutable
list is represented in the square brackets
'''


madhu=[2004,2,18,21,5.5,'manisha','madhu','madhumathi','gundu','reddy']
'''
print(madhu)
print(madhu[8],madhu[-8])
madhu_mathi=list()
print(madhu_mathi)
'''

'''
slicing in list
slicing is nothing but making into pieces
syntax of slicing in list is
[start:stop:skip]
'''
#type function is check the what the type of data it is

print(madhu[0:9:2])
madhuu=[]
print(type(madhu))

#to print all the elements in the list we can put semicolons

print(madhu[::])

# to reverse the list

print(madhu[::-1])
print(madhu[:])

print(madhu[:3])
print(madhu[3:])
print(madhu[5:0])
print(madhu[0:5:-8])

#to replace anything in the list

madhu[4]="dhonuru"
print(madhu)
