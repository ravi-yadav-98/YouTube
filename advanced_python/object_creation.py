'''
Object Creation in Python: How to control/customize

__new__():  to create objects in Python (can initialize attr too)

__init__(): Initializes attributes after Object Creation

'''

# class Person:
#
#     def __new__(cls, name, age):
#         if(age <0):
#             raise ValueError("age can not be negative")
#         print("1. Object Created ")
#         return super().__new__(cls)
#
#
#
#
# p  = Person('John', -29)
# print(p)


class Point:
    MAX_Inst = 3
    Inst_created = 0

    def __new__(cls,*args,**kwargs):
        if (cls.Inst_created >= cls.MAX_Inst):
            raise ValueError("Cannot create more objects")
        cls.Inst_created += 1
        print("Object: count ", cls.Inst_created, "created....")
        return super().__new__(cls)
    def __init__(self, x, y):
        self.x =x
        self.y = y



p1 = Point(1,2)
p2 = Point(2,2)
p3 = Point(3,4)
p4 = Point(6,5)
