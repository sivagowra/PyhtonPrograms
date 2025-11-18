class GrandParent:
    def fun3(self):
        print("This is grandparent class")
class Parent:
    def fun1(self):
        print("This is parent class")

class Child(Parent, GrandParent):
    def fun2(self):
        print("This is child class")

obj = Child()
obj.fun3()
obj.fun1()
obj.fun2()