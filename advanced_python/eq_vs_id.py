'''
Identity vs Equality in Python

identity: id()
     - object is given a unique identifier.
     - It's about whether two objects are the same object in memory.
      Checked using the is keyword or id() function.
      -  compare using "Is"

equality:   ==
    - Equality, on the other hand, refers to whether two objects
    have the same content or value. The == operator is used to
    check equality between objects.
    - __eq__() magic method in a class


'''

# a = [1,2, 3]
# b = a       #a--> X <---b
# print('id of a: ',id(a))
# print('id of b: ',id(b))
# b[0] = 10
# # print(a is b)
# print(a)

#
# a = [1,2,3]
# b = [1,2,3]
# print(a == b)
# print(a is b)
# print('id of a: ',id(a))
# print('id of b: ',id(b))




class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return  self.age == other.age

p1 = Person('A' , 21)
p2 = Person('A', 21)
print(p1 == p2)
print(p1 is p2)















