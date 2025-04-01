p="python \n programming"#normal string
print(p)
r=r"python \n programming" #raw string
print(r)

#the difference between noramal string and raw string is that in normal string escaping characters like \n is possible but in raw its not possible

import re #re means regular expression
address=" 17-1-382/p/56 road no:3 press colony champapet hyderabad 500079"
add_nos=re.findall(r'\d+',address)
print(add_nos)
add_2=re.findall(r'\d{2}',address)
print(add_2)
add_3=re.findall(r'\d{1,6}',address)
print(add_3)

#ip address pattern
s='''
<html>
<head>
<title>ip address</title>
</head>
<body>
ip address are 173.34.26.37
local address:137.43.62.73
computer 1: 736.24.34.26
computer 2: 472,44.13.35
computer 3: 534.24.55.56
</body>
</html>
'''
add_ip=re.findall(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}',s)
print(add_ip)