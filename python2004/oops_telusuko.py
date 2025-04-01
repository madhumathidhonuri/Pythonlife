class madhu:
    def mathi(self):
        print("hi")
reddy=madhu()
madhu.mathi(reddy)

class display:
    def show(self):
        print("hello")
info=display()
info.show()

class methods:
    def __init__(self):
        print("madhu")
app=methods()

class pen:
    def __init__(self,a,b):
        print("date and month {}-{}".format(a,b))
pencil=pen(18,3)


class paper:
    pages=45
    def __init__(self):
        self.type='single rule'
        self.cost=25
box=paper()
boxes=paper()
box.type='double rule'
print(box.type,box.cost,box.pages)
print(boxes.type,boxes.cost)

class student:
    school='TCHS'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def info(cls):
        return cls.school
    def something():
        print("this static class....")
s1=student(21,34,67)
s2=student(37,42,45)
print(s1.avg())
print(s2.avg())
print(s1.info())
student.something()


class nothing:
    def notin(self):
        print("1 working")
    def bedsheet(self):
        print("2 working")
class english(nothing):
    def notin(self):
        print("3 working")
    def bedsheet(self):
        print("4 working")
# s1=nothing()
# s1.notin()
# s1.bedsheet()
b1=english()
b1.notin()
b1.bedsheet()
        