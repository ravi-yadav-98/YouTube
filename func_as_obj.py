
'''
Video Title: Python Function as Objects

Important Points:
 - Everything in Python is an object so function is too an object
 - Objects has attributs(metadata) and methods (functionalites)
 - Object can be assigned to a variable, stored in data structure, and pass
 to a function or return from a function
  -

  In Python builtin "Object class" is baseclass for every object. (implicitly)

  Methods: __int__(), __repr__(), __str_(), __eq__(), __hash__(), __dir__
  Artributes: __dict__, __doc__, __module__, __class__

'''

class Temp:
    pass

def say_hello():
    return "Hello"

# print(isinstance(int, object))
# print(isinstance(str, object))
# print(isinstance(list, object))
# print(isinstance(float, object))
# print(isinstance(dict, object))
# print(isinstance(Temp, object))
# print(isinstance(say_hello, object))

# print(dir(say_hello))
# print()
# print(dir(object))


#assgn to a variable
func = say_hello
# print(func())
# print(func.__annotations__)
# print(func.__name__)

# del func

# print(func())


# arr = ['John', 10, say_hello]
# print(arr[2]())

# print(arr)

def get_name(func, name):
    print(func() + " " + name)


# get_name(say_hello, "Ramesh")


import time
#excetion

def get_execution_time(func):

    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()

        print("Execution Time:", end- start, 'sec')
    
    return inner

@get_execution_time
def run():
    for i in range(100):

        print(i)

# run()



def square(num):
    return num**2

def cube(num):
    return num*num*num
arr = [1,2,3,4,5]

sqr = list(map(square, arr))
# print(sqr)


# print(type(square))

funcs = {"square": square, "cube": cube}

print(funcs['square'](4))



