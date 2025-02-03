# . Create a `Product` class with attributes `name`, `price`, and `stock`. Write a method `check_availability(quantity)` that returns whether the requested quantity is available.
class Product():
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock
    def check_availability(self):
        self.get_input=input("enter the quantity name")
        return f"stock_name:{self.name} stock_price:{self.price} stock:{self.stock}"
pro=Product("tata","1000","nifty")
pro.check_availability()
print(pro.check_availability())
