class Item:
    pay_rate = 0.8
    def __init__(self,name:str,price:int,quantity:int):
        assert price >= 0, f"Price {price} is not greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to 0"


        self.name = name
        self.price = price
        self.quantity = quantity
        print(f"Created Instance {name}")
        
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate


item1 = Item("Phone",100,5)
# item2 = Item("Laptop",1000,3)
item1.apply_discount()


print(f"Before discount: {item1.price}")
print(f"After discount: {item1.price * item1.pay_rate}")

# print(item2.calculate_total_price())

# print(Item.__dict__)
# print(item1.__dict__)
# print(item2.__dict__)

