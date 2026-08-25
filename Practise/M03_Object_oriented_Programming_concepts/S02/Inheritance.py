'''
Inheritance : Acquring properties from one class to another class

Types of Inheritance:
1.Single
2.Multiple
3.Multilevel
4.Hierarchical
5.Hybrid
'''
'''
#Single Inheritance
class A :
    def displayA(self):
        print("Class A")
class B(A):
    def displayB(self):
        print("Class B")
a = A()  
b = B()
a.displayA()
b.displayB()
'''
#multilevel Inheritance
class A :
    def displayA(self):
        print("Class A")
class B(A):
    def displayB(self):
        print("Class B")
class C(B):
    def displayC(self):
        print("Class C")
a = A()
b = B()
c = C()
a.displayA()
b.displayB()
c.displayC()
