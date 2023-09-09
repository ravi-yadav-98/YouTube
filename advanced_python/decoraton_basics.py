'''
Decorators in Python:

Basics:
    - they are functions which modify the functionality of other functions.
    - enhance the behavior of functions or methods without changing their actual code.
    - Creates a wrapper function which takes a func as input and return the modifier version

This video:
 - Basics of Decorators
 - Simple Decorator creation

'''
#
# def greet(name):
#
#     def hi():
#         print("Hi")
#     def hello():
#         print('hello')
#
#     if name[0] =='A':
#         return hi()
#     else:
#         return  hello()


# fun = greet
# print(fun())

# def wrapper(func):
#     return func()

# greet('Smit')

def first_decorator(func):

    def wrapper(*args, **kwargs):
        print("Function Called....")
        func(*args, **kwargs)
        print("Function Successfully Executed")
    return wrapper



def welcome():
    print("You are welcome")

print(first_decorator(welcome()))