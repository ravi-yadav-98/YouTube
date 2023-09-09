'''
MappingProxy in Python:  __dict__

A dictionary or other mapping object used
to store an object’s (writable) attributes.


__dict__ contains the data stored in the program's memory for this specific object.


Everything is an object:
Function, Classes, Objects

Internals:
Obj.attr --> obj.__dict__['attr']


'''

class Person:
    country = "India"

    def __init__(self, name, age):
        self.name  = name
        self.age   = age

    def speak(self):
        print("I can speak Hind and English")


p = Person("Ramesh", 26)
print(p.__dict__)
# print(p.name)
print(p.country)

p.job = 'Engineer'
print(p.__dict__)
#
# Person.languge = "Hindi"
# print(Person.__dict__)











