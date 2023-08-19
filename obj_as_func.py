'''
Video Topic: How to use Objects as Functions:

All Functions are Objects but viceverca isn't true

__call__() : to make a object callable(function) : 

We can made a object callable by implementing __call__ method


'''
from typing import Any


def say_hello():
    return("hello")

# print(type(say_hello))
# print(isinstance(say_hello, object))
# print(callable(say_hello))

class Temp:
    
    def __call__(self):
        print("I am a callable object..")

obj = Temp()
# print(callable(obj))
# obj()


class Adder:
    def __init__(self, num) -> None:
        self.num = num 
    

    def __call__(self, num_to_add):
        return self.num + num_to_add
    
adder = Adder(10)
# for i in range(1, 10):
#     print(adder(i))


class Multiplyer:
    def __init__(self, factor) -> None:
        self.factor = factor
    
    def __call__(self, num):
        return num*self.factor


double = Multiplyer(2)
triple = Multiplyer(3)
half   = Multiplyer(.5)

# print(double(10))
# print(double(20))
# print(triple(20))
# print(half(100))



class Calculator:
    def __init__(self, operation:str) -> None:
        self.operation = operation
    
    def __call__(self, a, b):
        if self.operation.lower() == 'add':
            return a+b
        elif self.operation.lower() == 'substract':
            return a-b
        elif self.operation.lower() == 'multiply':
            return a*b
        elif self.operation.lower() == 'devide':
            if (b!=0):
                return a/b
            else:
                raise ValueError("Can not devide with zero")
        else:
            raise ValueError("No proper operation given")
    

adder         = Calculator('add')
substracter   = Calculator('substract')
multiplyer    = Calculator('multiply')
devider       = Calculator('devide')

print(adder(1,2))
print(substracter(10,2))
print(multiplyer(10,3))
print(devider(100, 4))




