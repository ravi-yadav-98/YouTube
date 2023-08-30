'''
Self:
- represent the instance of a class
- allow you to access attrs, methods of object
- self is not a Keyword
- Explicitly pass the obj reference to method

-
'''
# class MyClass:
#     def say_hello(self, name):
#         print("Hello, "+ name)

# obj = MyClass()
# # obj.say_hello() # MyClass.say_hello(obj)
# MyClass.say_hello(obj, "ravi")


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getAge(self):
        print(f"Age of Student  {self.name} is {self.age} ")

# s = Student('A' , 17)
# print(s.name)
# s.getAge()
# Student.getAge(s)



class MyClass:
    @staticmethod
    def say_hello():
        print("Hello, ")
# print(dir(MyClass))

obj = MyClass()


# obj.say_hello()
print(type(obj.say_hello))
print(MyClass.say_hello())

# MyClass.say_hello(obj)
# # print(dir(obj))
MyClass.say_hello()