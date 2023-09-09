'''
__slots__ in Python:

we know :
In Python objects are created dynamically,
 which means that their attributes can be added or removed at runtime
 (cost of memory usage and access speed)

__slots__ is a special attribute that can be added to a class to
restrict the attributes that can be added to its instances.

-  By using __slots__, you can tell Python to allocate memory for a fixed set
 of attributes, which can improve the performance of your code

-- attr stored in __slots__ not in __dict__

 Pros:
 1. Memory Optimization
 2. Improved Performance
 3. Attribute Name validation

 Cons:
 1. Inheritance
 2. No Dynamic Attributes
 3.  __dict__ won't work
'''
import  sys
class Person1:
    __slots__ = ('name')
    def __init__(self, name):
        self.name = name

# p1 = Person1('Amit')
#
# p1.age = 21
# print(p1.name)
# print(p1.age)
# print(p1.__dict__)

class Person2:
    __slots__ = ('name')
    def __init__(self, name):
        self.name = name
#
# p2 = Person2('Amit')
# p2.age = 21
# p2.height = 5.2
# print(p2.name)
# print(p2.age)
# print(p2.height)
# print(p2.__slots__)
# # print(p2.__dict__)

p1 = Person1('A')
# p2 = Person2('A')
# print('Allocated Memory for p1: ', sys.getsizeof(p1))
# print('Allocated Memory for p2: ', sys.getsizeof(p2))

# p1.name = 'Aaa'
p1.name = 'Aaa'
print(p1.name)



class Point1:
    __slots__ = {
        'x' : "Coordinate x",
        'y' : "Coordinate y",
        '__dict__' : 'mapping dictionary'
    }
    def __init__(self, x, y):
        self.x = x
        self.y = y


# p = Point1(1,2)
# p.z = 3
# print(p.x)
# print(p.y)
# print(p.z)
# print(help(Point1))





















