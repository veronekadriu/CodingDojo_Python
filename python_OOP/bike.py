# This class creates a bike with some methods and atributes
class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.initial_miles=0
    def displayinfo(self):
        print("Bike's price is: ", self.price)
        print("Bike's maximum speed is: ", self.max_speed)
        print("Bike's total miles: ", self.initial_miles)
        return self
        
    def ride(self):
        print ("Riding")
        self.initial_miles += 10
        return self

    def reverse(self):
        print ("Reversing")
        self.initial_miles -= 5
        if self.initial_miles <0:
            self.initial_miles =0
        return self
        
bike1 = Bike(200, "25mph").ride().ride().ride().reverse().displayinfo()

bike2 = Bike(500, "30mph").ride().ride().reverse().reverse().displayinfo()

bike3 = Bike(600, "60mph").reverse().reverse().reverse().displayinfo()
     

