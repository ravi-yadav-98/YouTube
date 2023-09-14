'''
Name Mangling: 

A technique used to make the names of attributes 
in a class more "private". 
This means that they are harder to access  from outside the class. 

When you prefix a variable or method name with double underscores
(e.g., __variable), Python performs name mangling.

Internal changes the name: _ClassName__variable

Note:
- Name mangling is a convention, not a strict rule. 
- It's still possible to access these variables and methods 
if you know their mangled names
- Do  only if your have good reason to do


'''
class Circle:

    def __init__(self, radius) -> None:
        self.__radius = radius
    
    def __getDiameter(self):
        return self.__radius*2
    
    def getRadius(self):
        print("radius is: ", self.__radius)

c = Circle(6)
# c.getRadius()
print(c._Circle__radius)
# print(dir(c))
print(c._Circle__getDiameter())
