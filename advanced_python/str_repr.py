'''
Object String Representations in Python : __str__ and __repr__ methods


Why:
- This method allows you to provide a user-friendly representation of the object, making it easier to understand the object's content.
- 

__str__
    :  User-readable string representation of the object. (imformal)
    : called by print() or str()  
    

__repr__
    : intended for machine readability.(developer friendly) : formal
    : valid Python expression that can be used to recreate the object (eval() method).
    : called by repr() function
'''

# s = "Hello World"
# a = 10
# print(str(a))

# class MyClass(object):
#     x = 1

#     def __str__(self):
#         return f"value of x: {self.x}"


# obj = MyClass()
# print(obj)


class Point(object):
    def __init__(self, x, y) -> None:
        self.x = x 
        self.y = y
    
    def __str__(self) -> str:
        return f'Coorinate is: ({self.x}, {self.y})'

    def __repr__(self) -> str:
        return f'Point(x={self.x}, y={self.y})'
    

point    = repr(Point(x=2, y=12))
newPoint = eval(point)
print(isinstance(newPoint, Point))
print(newPoint)


