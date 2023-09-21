'''
__index__ in python: Convert a Object to Integer Representation

Usecase:
 - Use as index: Object for slicing (PEP: 357)
 - Conversions (bin, hex etc)


'''

# print(s[1:3])
# print(bin(3))

class CustomInteger:
    def __init__(self, val) -> None:
        self.val = val
    
    def __index__(self):
        return self.val

s = "Hello World"
obj1 = CustomInteger(3)
obj2 = CustomInteger(5)
# print(bin(obj1))
# print(hex(obj1))
print(s[obj1: obj2 ])

