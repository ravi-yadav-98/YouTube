'''
Object Inspection in python:

Know details about your objects

Use Standard functions:
 - type, dir, id, hasattr, issubclass,  isinstance,

The Inspect Module:

The inspect module provides several useful functions to help get
information about live objects such as modules, classes, methods,
 functions.


'''
# s = "hello world"
# print(type(s))
# print(dir(s))
# print(id(s))
# print(isinstance(s, str))
# print(s.__doc__)

class Student:
    '''
    A class to represent Students
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def printAge(self):
        print("Age of Student: ", self.age)

s1 = Student('A', 12)
# s2 = Student('B', 17)
# print(type(s1))
# # print(dir(s1))
# print(isinstance(s2, Student))
# # print(s1.__doc__)
def fun():
    return "hello"
import  inspect
import  math

#validate
# print(inspect.isclass(Student))
# print(inspect.ismodule(math))
# print(inspect.isfunction(fun))
# print(inspect.ismethod(s1.printAge))


#info
# print(inspect.getsource(Student))
print(inspect.getdoc(Student))
print(inspect.getmembers(s1))


