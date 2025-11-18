class A:
    def __init__(self):
        print("This is class A")

class B(A):
    def __init__(self):
        print("This is class B")
        super().__init__()

class C(B):
    def __init__(self):
        print("This is class C")
        super().__init__()      

obj = C()