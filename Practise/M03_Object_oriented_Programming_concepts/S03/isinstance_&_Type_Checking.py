'''
type() function is used to check the type of an object. It returns the type of the object passed as an argument. 
The isinstance() function is used to check if an object is an instance of a specific class or a subclass thereof. It returns True if the object is an instance of the specified class or its subclass, and False otherwise.
'''
a=10
b=5.6
c="Hello"
d=[1,2,3]
e=(1,2,3)
f={1,2,3}
g={'name':'John', 'age':30}
print(type(a))  
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))

#checking multiple values:
x="Ram"
if isinstance(x, (int, float, str)):
    print("x is either an integer, float, or string")
else:
    print("x is not an integer, float, or string")

#checking with classes
class Animal:
    pass
class Dog(Animal):
    pass
class Cat(Animal):
    pass
d=Dog()
c=Cat()
print(isinstance(d, Dog))  # Output: True
print(isinstance(d, Animal))  # Output: True
print(isinstance(c, Cat))  # Output: True

#duck typing: same methiod acts as same behaviour for different classes
class dog:
    def sound(self):
        return "Woof"
class cat:
    def sound(self):
        return "Meow"
def make_sound(animal):
    print(animal.sound())
d=dog()
c=cat()
make_sound(d)  # Output: Woof
make_sound(c)  # Output: Meow

#Example
def process(data):
    if isinstance(data, list):
       return data*2
    elif isinstance(data, str):
       return data.upper()
    elif isinstance(data, int):
       return data + 10.5
print(process(10))
print(process("Kedhar"))
print(process([1, 2, 3]))

#inteview question:
class A:
    pass
class B(A):
    pass
obj = B()
print(type(obj)==B)
print(type(obj)==A) 
print(isinstance(obj, B))
print(isinstance(obj, A)) 
