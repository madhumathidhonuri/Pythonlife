# madhu=["EVEN" if i%2==0 else "ODD" for i in range(10)]
# print(madhu)
'''
madhu=[3,76,9,9,9,8,8,8,7,2,8]
n=[]
for i in madhu:
    if i==9:
        madhu.remove(9)
    else:
        n.append(1)
print(n)
'''
'''
x=int(input())
y=int(input())
z=int(input())
n=int(input())
for i in range(x):
    pass
    for j in range(y):
        pass
        for k in range(z):
            pass
print([i,j,k])
'''

StudentID=[1,2,3,4,5]
Subject1=[89,90,78,93,80]
Subject2=[90,91,85,88,86]
Subject3=[91,92,83,89,90.5]
Average=[90,91,82,90,85.5]
a=zip(StudentID,Subject1,Subject2,Subject3,Average)
print(a)
