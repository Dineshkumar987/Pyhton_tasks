# Base class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

# Derived class
class Car(Vehicle):
    def display(self):
        print("Car Brand:", self.brand)
        print("Speed:", self.speed, "km/h")
        print()

# Derived class
class Bike(Vehicle):
    def display(self):
        print("Bike Brand:", self.brand)
        print("Speed:", self.speed, "km/h")
        print()

# Creating objects
car = Car("Toyota", 180)
bike = Bike("Yamaha", 120)

# Display details
car.display()
bike.display()