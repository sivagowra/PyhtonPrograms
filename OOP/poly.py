#method overloading
class A:
    def sum(self,a,b):
        return a+b

class B(A):
    def sum(self,a,b,c=1):
        return a*b*c

obj = B()
print(obj.sum(10,20))
print(obj.sum(10,20,30))

# method overriding

class C:
    def display(self):
        print("This is class C")

class D(C):
    def display(self):
        print("This is class D and calling parent class method")
        super().display()

obj = D()
obj.display()