#   single inheritance=one child and one parent class

class Parent():
    def output(self):
        print("this is parent class")
class Child(Parent):
    def childoutput(self):
        print("this is child class")
i=Child()
i.childoutput()
i.output()



#   multiple inheritance=one child and two parent classes
'''
class Father():
    def output(self):
        print("this is parent class")
class Mother():
    def outputm(self):
        print("this is parent class 2")
class Child(Father,Mother):
    def childoutput(self):
        print("this is child class")
ice=Child()
ice.childoutput()
ice.outputm()
ice.output()
'''


#  multilevel inheritance=levels
'''
class Grandfather():
    def output(self):
        print("this is parent class 1")
class Father(Grandfather):
    def outputf(self):
        print("this is parent class 2")
class Mother(Father):
    def outputm(self):
        print("this is parent class 3")
class Child(Mother,Grandfather):
    def childoutput(self):
        print("this is child class")
mad=Child()
mad.childoutput()
mad.outputm()
mad.outputf()
mad.output()
'''

# hirarical inheritance=one parent class and more child classes
'''
class Father():
    def output(self):
        print("this is parent class")
class Child1(Father):
    def output1(self):
        print("this is child class 1")     
class Child2(Father):
    def output2(self):
        print("this is child class 2")
ice=Child1()
cream=Child2()
ice.output()
cream.output()
ice.output1()
cream.output2()   
'''


