madhu=[2,18,2004,21,3,7,2,26,2003,22,28,4,2003]
# variable.method()
'''
append method is used to add the element at end of the list
'''
# madhu.append(2015)
# print(madhu)

'''
extend method is also used to add data at last to list but in separate form
'''
# madhu.extend([7,0,1])
# print(madhu)

'''
count method is used to count the data in the list
'''
#print(madhu.count(2004))

'''
clear method is clear the data from the list
'''
# madhu.clear()
# print(madhu)

'''
copy method is used to copy the data from the list
'''
# manisha=madhu.copy()
# madhu.append(12) # hear 12 will not be added to the list because it is a copied list
# print(manisha)

'''
index method is used to find the index position
'''
# print(madhu.index(21))

'''
length method is used to find the length of the list
it is built in data type
'''
# print(len(madhu))

'''
insert method is used to insert the data into the list at the position which we want
insert(location,element)
'''
#madhu.insert(4,15)
#print(madhu)

'''
pop method is used to pop the element from the list
pop method uses location of the element to delete
'''

#madhu.pop(0)
#print(madhu)

'''
remove method is used to remove the element from the list
remove method uses element to remove the element 
'''
# madhu.remove(2004)
# print(madhu)

'''
reverse method is used to reverse the list
'''
# madhu.reverse()
# print(madhu)

'''
sort method is used to sort the elements in the list in ascending or descending order
to sort in descending order use reverse=true
'''
#madhu.sort() #ascending order
#print(madhu)
# madhu.sort(reverse=True) #descending order
# print(madhu)