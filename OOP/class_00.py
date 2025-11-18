class Car:
    def __init__(self,name,year,rate):
        self.name=name
        self.year=year
        self.rate=rate
    def display(self):
        print("Name:", self.name)
        print("Year:", self.year)
        print("Rate:", self.rate)
obj1=Car("TATA", 2022, 2000000)
obj1.display()
print("-----------------------------------------")
obj2=Car("Mahendra", 2025, 450000)
obj2.display()
 


        