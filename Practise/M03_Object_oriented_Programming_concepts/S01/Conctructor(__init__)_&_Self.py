from math import pi
class circle:
    def __init__(self, r):
        self.r = r
    def area(self):
        return pi*self.r**2
    def circumference(self):
        return 2*pi*self.r
c1=circle(7)
c2=circle(5)
c3=circle(3)
print("Area of circle 1:",c1.area())
print("Circumference of circle 1:",c1.circumference())
print("Area of circle 2:",c2.area())
print("Circumference of circle 2:",c2.circumference())
print("Area of circle 3:",c3.area())
print("Circumference of circle 3:",c3.circumference())


#1603.Design Parking System
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType == 1 and self.big > 0:
            self.big -= 1
            return True
        elif carType == 2 and self.medium > 0:
            self.medium -= 1
            return True
        elif carType == 3 and self.small > 0:
            self.small -= 1
            return True
        else:
            return False
parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))  
print(parkingSystem.addCar(2))  
print(parkingSystem.addCar(3))  
print(parkingSystem.addCar(1))

#1603. Design Parking System
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {
            1: big,
            2: medium,
            3: small
        }

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False
parkingSystem = ParkingSystem(1, 1, 0)
print(parkingSystem.addCar(1))
print(parkingSystem.addCar(2))
print(parkingSystem.addCar(3))
print(parkingSystem.addCar(1))