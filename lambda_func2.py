'''
Lambda Function in Pyhon: Part: 01 basci usecases

concise way to define small, anonymous functions using a compact syntax.


Usecases:
1. Higher order function 
2. Lambda with decorators
3. Nested Lambda function : function factory
4. function compositiom  f(g(x))
'''

#Higher order function 


def power(exponent):
    return lambda x: x**exponent


# power_2 = power(2)
# power_3 = power(3)
# power_4 = power(4)
# power_5 = power(5)
# input =  int(input("enter a num"))
# print('power_2: ', power_2(input))
# print('power_3: ', power_3(input))
# print('power_4: ', power_4(input))
# print('power_5: ', power_5(input))


# def say_hello(func):
#     return lambda name: "Hello " + func(name)



# def say_hello(func):

#     def wrapper(name):
        
#         output = "Hello  " + func(name)
#         return output
    
#     return wrapper

# @say_hello
# def get_name(name):
#     return  name


# name =  input("enter your name")
# # print(get_name(name))


# def operation(op):
#     return lambda x, y: x+y if op=='add' else x-y


# operation = lambda op: (lambda x, y: x+y if op=='add' else x-y)
# op1 = operation('add')
# op2 = operation('sub')

# print(op1(2,3))
# print(op2(4,6))

compose = lambda f,g, h: lambda x: h(f(g(x)))

add_2  = lambda x: x+2  #f
sq     = lambda x: x**2  #g 
div    = lambda x: x/10

transform = compose(add_2, sq, div)

print(transform(5))