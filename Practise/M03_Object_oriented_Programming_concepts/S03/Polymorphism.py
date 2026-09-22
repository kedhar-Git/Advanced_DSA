'''
Polymorphism : One name, many forms 
In Python, polymorphism refers to the way in which different object classes can share the same method name, but those methods can act differently based on which object calls them. This allows for flexibility and the ability to define methods in a way that is specific to the object that is calling them.
It is of two types:
1. Compile time polymorphism (Method Overloading)
2. Run time polymorphism (Method Overriding)
Method Overloading : In Python, method overloading is not directly supported as it is in some other programming languages. However, you can achieve similar functionality by using default arguments or variable-length arguments in your methods. This allows you to define a single method that can handle different numbers of arguments or different types of arguments.
Method Overriding : Method overriding is a feature in object-oriented programming that allows a subclass to provide a specific implementation of a method that is already defined in its superclass. When a method in a subclass has the same name, return type, and parameters as a method in its superclass, the subclass's method overrides the superclass's method. This allows for dynamic polymorphism, where the method that gets executed is determined at runtime based on the object's actual type.
'''
class A:
    def display(self):
        print("Class A")
class B(A):
    def display(self):
        print("Class B")

a = A() #object of class A
b = B() #object of class B

a.display()  # Output: Class A
b.display()  # Output: Class B  

#type checking
print(isinstance(a, A))  # Output: True 