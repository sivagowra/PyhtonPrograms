class Father:
    def fun1(self):
        print("This is father class")

class Mother:
    def fun2(self):
        print("This is mother class")

class Child(Father, Mother):
    def fun3(self):
        print("This is child class")

obj = Child()
obj.fun1()      
obj.fun2()
obj.fun3()