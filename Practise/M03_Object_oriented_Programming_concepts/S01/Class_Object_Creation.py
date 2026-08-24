from math import pi
class circle:
    r=7
    def area(self):
        return pi*self.r**2
    def circumference(self):
        return 2*pi*self.r
c=circle()
print("Area of circle:",c.area())
print("Circumference of circle:",c.circumference())