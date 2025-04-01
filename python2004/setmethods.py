s={'madhu',1,5,18}
# print(type(s))
# m={}
# print(type(m))
'''
set is a unordered and unindexed
that means it stores elements randomly and it does not take indexes
'''
print("***set methods***")
print("add method:")
s.add(2003)
print(s)
print("copy method")
s.copy()
print(s)
print("pop method:")
s.pop()
print(s)
print("remove method:")
s.remove('madhu')
print(s)
print("update method:")
s.update([1,3,5,18,34,65])
print(s)
s.update({1,5,34,9,8,656,343,2135})
print(s)
s.update((2324354,'22D41A0561',40564,6281670029))
print(s)
print("clear method:")
s.clear()
print(s)