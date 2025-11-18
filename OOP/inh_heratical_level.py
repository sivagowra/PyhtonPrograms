class Parent:
    def fun1(self):
        print("This is parent class")

class Child1(Parent):
    def fun2(self):
        print("This is child class")
class Child2(Parent):
    def fun3(self):
        print("This is child2 class")
obj = Child1()
obj.fun1()
obj.fun2()
# obj.fun3()