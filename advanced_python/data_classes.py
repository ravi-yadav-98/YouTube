'''
data classes in python: >=3.7
a simple way to create classes primarily used for storing data.

They automatically generate common methods
like __init__(), __repr__(), __eq__(),
and others, saving you from writing boilerplate code.

ex: Point(x,y)

Notes:
    1. Conciseness
    2. Readability
    3. Not for complex classes
'''
from dataclasses import  dataclass, field

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y =y
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    def __eq__(self, other):
        return self.x == other.x  and self.y == other.y


# p1 = Point(1,2)
# p2 = Point(1,2)
# print(p1)
# print(p1 == p2)

@dataclass(frozen=True)
class PointXY:
    x: int
    y: int = field(default=-10, repr=False)

p1 = PointXY(2, 3)
# p2 = PointXY(22)
# p1.x = 4
print(p1)
# print(p1 == p2)




@dataclass
class Person:
    name: str
    age: int
    address:str
@dataclass
class Student(Person):
    mark:float
    std:int

s1 = Student('Aman', 12, 'XYZ', 70, 8)
print(s1)
