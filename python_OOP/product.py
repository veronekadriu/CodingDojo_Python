# The owner of a store wants a program to track products. This class creates a product class
class Product:
    def __init__(self,price,item_name,weight,brand,status):
        self.price =price
        self.item_name =item_name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.status = "for sale"

    def sell(self):
        self.status = "sold"

    def add_tax(self, tax):
        self.price = self.price * tax
    

    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status= "used"
            self.price = 0
        elif reason_for_return == "like new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "used"
            self.price = self.price*0.8
    
    def display_info(self):
        print ("Item Name: ", str(self.item_name))
        print ("Brand: " , str(self.brand))
        print ("Price: ", str(self.price))
        print ("Weight: ", str(self.weight)) 
        print ("Status: " ,self.status ,"\n")

coca_cola = Product(5, "Coca Cola", 5, "Coca Cola", "for sale")
coca_cola.add_tax(1.5)
coca_cola.sell()
coca_cola.display_info()
shoes= Product(50, "Timberland", 10, "Timberland", "for sale")
shoes.return_item("defective")
shoes.display_info()

