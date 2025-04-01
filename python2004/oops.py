'''
oops is based on the concept of objects
objects are nothing but data and Code
data means variables and code means function
'''
#   TYPES OF OOPS
'''
1)objects
2)encapsulation
3)polymorphism
4)abstraction
5)inheritance
6)class

'''
#oops terminology
'''
ATTRIBUTE is also known as data member or variable
BEHAVIOR is also known as member function or method

'''
#class
'''
class is a collection of objects
it binds data members and methods into single unit
it is a blue print for object creation

'''
#object
'''
objectt is a collection of data variables and methods
object is real time entity(physical)
object is a instance of class
process of creating object is known also instantiation

'''


class Madhu():#class defination
    def fruits(self): #self keyword is used access the attributes and methods of the current class only
        print("i am madhu,i like fruits")
mathi=Madhu()#object creation     object name=class name()
mathi.fruits()#to access methods  object name.method()


class Madhuu():
    a=18
    def show(self):
        print("i am madhumathi from cse department")
mad=Madhuu()
print(mad.a)
mad.show()


class Madhumathi():
    a=2004
    def madhu(self):
        print("bunnyyy")
bunny=Madhumathi()
bunny.madhu()
print(bunny.a)

class Bunny():
    a=2003
    def ammulu(self):
        print(self.a)
raju=Bunny()
raju.ammulu()

#multiple object creation

class Raju():
    a=26
    def pilla(self):
        print(self.a)
sri=Raju()
bun=Raju()
sri.pilla()
bun.pilla()


class Rajuu():
    def __init__(self,a,b):
        self.aa=a
        self.bb=b
        print(a)
        print(b)
        print(a+b)
        print(a-b)
        print(a*b)
        print(a/b)
        print(a%b)
    def Rajj(self):
        print(self.aa,self.bb)
m=Rajuu(1,1)
m.Rajj()


#mobiles using init
class Mobiles():
    def __init__(self,mobile_name,mobile_RAM,mobile_battery,mobile_price):
        self.a=mobile_name
        self.b=mobile_RAM
        self.c=mobile_battery
        self.d=mobile_price
    def Moblies_data(self):
        print("mobile name=",self.a)
        print("mobile RAM=",self.b)
        print("mobile battery=",self.c)
        print("mobile price=",self.d)
#while True:#dynamic memory allocation
name=input("enter the mobile name:")
ram=input("enter the mobile ram:")
battery=input("enter the mobile battery:")
price=input("enter the mobile price:")
Mobile_obj=Mobiles(name,ram,battery,price)
Mobile_obj.Moblies_data()
    
#bikes using init
class Bikes():
    def __init__(self,bike_name,bike_price,bike_warranty):
        self.a=bike_name
        self.b=bike_price
        self.c=bike_warranty
    def bike_data(self):
        print("bike name=",self.a)
        print("bike price=",self.b)
        print("bike warranty=",self.c)
name=input("enter the bike name:")
price=int(input("enter the bike price:"))
warranty=input("enter the warranty:")
Bikes_obj=Bikes(name,price,warranty)
Bikes_obj.bike_data()
