'''
string is a sequence of characters
string is defined in 3 ways
i.e is
'', " " ,''' '''
when we use single quotes we can't keep apastaphi 
we can't write a paragraph in double quotes
paragraph is possible in triple quotes
'''

#string methods

# madhu="i am madhumathi my nick name is manisha i am studying in sri indu"

# print(madhu.upper()) # upper method is used to change the lower case letters to upper case letters

# print(madhu.lower()) #lower methid is used to change the upper case letters to lower case letters

# print(madhu.count("i")) # count method is used to count the no of strings

# print(madhu.startswith("i")) # the startswith method returns output true when the string starts with the starting string

# print(madhu.endswith("sri")) #the endswith method returns output true when the string ends with the last string

# print(madhu.find("madhu"))#find method finds the index position

# print(madhu.index("a"))


madhu=["abc.in","xyz.com","def.in"]
'''
in_madhu=[]
for i in ["abc.in","xyz.com","def.in"]:
    if i.endswith("in"):
        in_madhu.append(i)
print(in_madhu)

'''
# format function

# names=["madhu","bindu","srikanth","navya","bunny","chintu","sudheer"]
# for i in names:
#     print("hi {} ! thinnara?".format(i))

# a="madhu"
# print(a.isalnum())
# print(a.isalpha())
# print(a.isnumeric())


d=madhu.split()
print(d)
s="@".join(d)
print(s)
# print(madhu.replace("myself","i am"))
# e=madhu.replace("myself","i am").replace("are","like")
# print(e)

# madhu="  i am madhumathi i am studying in sri indu clg   "
# print(len(madhu))
# d=madhu.rstrip()
# print(d)
# print(len(d))
# e=madhu.lstrip()
# print(e)
# print(len(e))

# madhu="love story of romantic couple"
# print(madhu.title()) #changes the first lower case to upper case in every word like how the book titles will be 

madhu="myself madhumathi i are funny movies"
n=[]
for i in madhu:
    if i=="myself":
        i=="i am"
        n.append(i)
    else:
        n.append(i)
print(n)





