'''
Operator Overloading in Python:
- Python that allows the same operator to have different
meaning according to the context is called operator overloading.

- same operator behaves differently with different types.


common operators
__add__()
__sub__()
__mul__()
__pow__()

'''

# example + operator
# print(2 + 3)
# print("abc" + "dfe")
# print([1,2,3] + [4,5,6])

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        newX = self.x + other.x
        newY = self.y + other.y
        return Point(newX, newY)

    def __sub__(self, other):
        newX = self.x - other.x
        newY = self.y - other.y
        return Point(newX, newY)

    def __str__(self):
        return f'({self.x}, {self.y})'


p1 = Point(1,3)   #1+3, 3+5
p2 = Point(3, 5)
print(p1-p2)

