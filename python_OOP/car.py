# Creates a class called car
class Car:
    def __init__(self, price,speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price <= 10.000:
            self.tax = 0.12
        else:
            self.tax = 0.15
        self.display_all()
    
    def display_all(self):
        print("Price: ", str(self.price))
        print("Speed: ", str(self.speed))
        print("Fuel: ", str(self.fuel))
        print("Mileage: ", str(self.mileage))
        print("Tax: ", str(self.tax), "\n", "*"*50)

car1 = Car(2000,"35mph", "Full", "15mpg")
car2 = Car(2000,"5mph", "Not Full", "105mpg")
car3 = Car(2000,"15mph", "Kind of Full", "95mpg")
car4 = Car(2000,"25mph", "Full", "25mpg")
car5 = Car(2000,"45mph", "Empty", "25mpg")
car6 = Car(200000000,"35mph", "Empty", "15mpg")
