print("***       set operationns         ***")

set1={6,80,754,77534,665456,"madhu",9987}
set2={9,8,7,6,5,67,986,763}

print("union operation:")#removes duplicates
print(set1.union(set2))

print("intersection operation:") #prints common elements
print(set1.intersection(set2))

print("difference operation:") #substracts common elements and prints remaining elements
print(set1.difference(set2))

print("symmetric difference:") #remove common elements
print(set1.symmetric_difference(set2))

print("disjoint operation:")  #no same data in two sets
print(set1.isdisjoint(set2))
print(set2.isdisjoint(set1))

print("subset operation:") #subset means child 
print(set1.issubset(set2))

print("superset operation:") #superset means parent
print(set1.issuperset(set2))



for i in {5,886,8075,6532,532,6543,98}:
    if i==6532:
       print(i)
       break
    else:
       print('no')

madhu=[5,7,3,5,2]
s=frozenset(madhu)
print(s)
print(type(s))
    