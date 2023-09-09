'''
None in Python:

- Python uses the keyword None to define null objects and variables.
-  types.NoneType: class object
- None is frequently used to represent the absence of a value
- Not same as null
- Not similar to , False, 0, '', [], {}
- we can use == or Is to compare none
- singleton object
-


Application:
1. Default Parameter
2. Function with no return type
3. Initialize None variable



'''

a     = None
b     = None
str   = None

# print(id(a))
# print(id(b))
# print(id(str))

# s = None
# s1 = ''
#
# print(None == '')
# print(None == [])
# print(None == 0)

def say_hello() ->None:
    print("Hello")

# print(say_hello())

def ask_name(firstName, lastName = None):
    if lastName is  None:
        return  firstName
    else:
        return firstName + " " + lastName


name = ask_name("Amit", 'Tiwari')
print(name)


