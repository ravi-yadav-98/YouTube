'''
Namespaces in python:
 -  the structures used to organize the symbolic names assigned to objects in a Python program.
 -  names refer to some object (name binding)
 -  python tracks all names in your code using namespaces
 - Python executes a program, it creates namespaces as necessary 
 and deletes them when they’re no longer needed.
 - 

 
 4 types of namespaces: Defined on Scope of names

 Built-In : contains the names of all of Python’s built-in objects
 Global   : contains any names defined at the level of the main program.
          : it remains in existence until the interpreter terminates.
 
 Enclosing: names of enclosing function (nested function)
 Local    : names of local variable in a function
          : existence until its respective function terminates

'''
#builtin namespace
# print(dir(__builtins__))

#global
name = 'Ravi'

def square(num):

    a = 10   #local namespace
    # print(dir())
    return num**2

square(2)
# print(dir())


class Person:
    country = 'India'
    def __init__(self, name, age) -> None:
        self.name = name 
        self.age = age

p = Person("Rama", 21)
# print(dir(p))

def outer():  #encloing 
    num = 20
    print(dir())
    def inner():  #enclosed
        # num = 30  #local
        print(num)
    
    inner()

outer()

