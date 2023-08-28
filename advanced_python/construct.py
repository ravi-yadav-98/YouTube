'''
Understanding __init__() in Python :

Constructor: a method which creates object of a class
__init__() initializes attributes of the instance after creation,
        :- High level initialization of attributes

__new__() is responsible for the creation of the instance itself.
           -: Allocate memory to instance
           -: Low level

__new__() is called before __init__()

'''

class Person(object):

    def __new__(cls, name ='ravi', age=27):
        print(cls)
        print("1. Object Created....")
        instance = super().__new__(cls)
        instance.name = name
        instance.age = age
        return instance
    # def __init__(self, name = 'John', age =27):
    #     print("2. Object Attributes initialized")
    #     self.name = name
    #     self.age = age



p = Person()
print(p.name)
print(p.age)


