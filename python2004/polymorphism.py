#polymorphism means poly means many morphism means from


#methodoverload
'''
class Methodoverload():
    def output(self,a=None,b=None,c=None):
        print(a,b,c)
o=Methodoverload()
o.output(1,2,3)
o.output(1,2)
o.output(1)
o.output()
'''


#methodoverriding

class Methodoverride():
    def output(self):
        print("this is parent class")
class Child(Methodoverride):
    def output(self):
        print("this is child class")
        super().output() # super is used to access the parent class
i=Child()
i.output()


# encapsulation

#protected means single underscore
'''
class Gfather():
    def __init__(self,a):
        self._y=a  # single underscore _ protected
        print(self._y)
class Father(Gfather):
    def output(self):
        print(self._y)
class Child(Father):
    def outputchild(self):
        print(self._y)
i=Child(12)
i.outputchild()
i.output()
'''

#private means double underscore __ only one class can access
"""
class Gfather():
    def __init__(self,a):
        self.__y=a  # only this can access when it is private
        print(self.__y)
class Father(Gfather):
    def output(self):
        print(self.__y)
class Child(Father):
    def outputchild(self):
        print(self.__y)
i=Child(12)
i.outputchild()
i.output()
"""



#abstraction
'''
no body
class cannot create object
two or more classes is said to be ABC class
'''
'''
from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod  #decorator
    def mileage(self):
        pass
class Aulto(Car):
    def mileage(self):
        print("mileage 40")
class Innova(Car):
    def mileage(self):
        print("mileage 60")
a=Aulto()
a.mileage()
i=Innova()
i.mileage()
'''