a=(1,2,18,26,28,4,3,211,22.5,30.55)
# print(type(a))
#print(list(a))
'''
built in functions
print(len(a))
print(max(a))
print(min(a))
print(sum(a))
'''

#tuple operations
'''
concatenation

m1=(18,26,28)
m2=(2,2,4)
#print(m1+m2)
m=zip(m1,m2)
#print(tuple(m))
n=[]
for i,j in zip(m1,m2):
    print(i+j)
    n.append(i+j)
print(tuple(n))

'''
# membership operator

d=(1,3,2,4,56,4,7,4,63,5434,'madhu')
print(56 in  d)
print(48  not in  d)

# identity operator
t1=(1,2,3)
t2=(1,2,3)
print(t2  is t1)
t3=(4,5,6)
t4=(7,8,9)
print(t3 is not t1)

