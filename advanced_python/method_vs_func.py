'''
Function vs Method : Difference


Function:
 - a block of reusable code that performs a specific task.
 - can be called as func_name()
 - self-Contained: not bound to any object
 - tale input parameters

Method:
  - A method is a function that is associated with an object or a class
  - called using object.method_name()
  - first argument is self
  - Bound to an Object
'''

def greet(name):
    print( "Hello " + name)

# greet('ravi')
# print(type(greet))

class MyClass:
    def greet(self, name):
        print("Hello " + name)

obj= MyClass()
print(type(obj.greet))
# obj.greet("ravi")